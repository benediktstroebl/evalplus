```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    A list is monotonically increasing if for every pair of adjacent elements, the
    first is not greater than the second. A list is monotonically decreasing if
    for every pair of adjacent elements, the first is not less than the second.

    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    is_increasing = all(i <= j for i, j in zip(l, l[1:]))
    is_decreasing = all(i >= j for i, j in zip(l, l[1:]))
    return is_increasing or is_decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the elements in the list are monotonically increasing or decreasing, and `False` otherwise. The function uses the `all` function with a generator expression to check if the list is monotonically increasing or decreasing. If the list is either increasing or decreasing, the function returns `True`; otherwise, it returns `False`. The script also includes test cases to verify the correctness of the function.