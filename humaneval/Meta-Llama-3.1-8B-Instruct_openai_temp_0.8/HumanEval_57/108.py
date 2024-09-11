```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([5, 5, 5, 5]))  # Expected output: True
print(monotonic([1, 2, 1, 3]))  # Expected output: False
```

This script uses the `all` function to check if all pairs of adjacent elements in the list are related (either in the sense that `a <= b` or `a >= b` for all pairs `(a, b)`). The list is checked for both increasing and decreasing order. If the list is empty, the function will return `True` since an empty list is considered to be both increasing and decreasing.