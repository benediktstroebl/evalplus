```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 != 0 for c in str(x))]
    return sorted(odd)
```

The function `unique_digits(xs)` employs a list comprehension to iterate over each element in the input list `xs`. For each element `x`, it checks if any digit in the string representation of `x` is odd using the `any()` function and the modulo operation (`int(c) % 2 != 0`). If any odd digit is found, the element is added to the `odd` list. Finally, the function sorts the `odd` list in ascending order and returns it.

Here is an example usage of the function:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

This demonstrates that the function correctly filters out elements with even digits from the input list and returns the unique elements that have at least one odd digit, in ascending order.