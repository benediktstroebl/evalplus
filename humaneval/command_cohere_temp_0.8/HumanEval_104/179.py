```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an input and returns a sorted list of all elements that do not have any even digits. This is done using a list comprehension that iterates over each element in the input list `xs`, and for each element `x`, it checks if any digit in the string representation of `x` is even, using the `any()` function and a generator expression. If no even digits are found, it includes `x` in the resulting list, which is then returned. The `sorted()` function ensures that the returned list is always sorted in increasing order. 

You can test this function with the following calls:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

This should return the expected output according to the note in the problem description.