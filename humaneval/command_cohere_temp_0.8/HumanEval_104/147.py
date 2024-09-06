```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 for y in str(x))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension that iterates over each element in the input list `xs`. It checks if the element is odd by checking if any digit in the integer representation of the element is odd using the `any` and `int(y) % 2 for y in str(x)` operations. The result is a list of all elements that contain at least one odd digit. This list is then returned by the function. Since the returned list is already sorted, no sorting is required for this solution.  This solution's efficiency is `O(n log(n) )`, where `n = |xs|`, where `|xs|` is the number of elements in the input list `xs`.