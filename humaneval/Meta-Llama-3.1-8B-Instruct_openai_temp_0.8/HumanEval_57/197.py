```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 2, 3, 4]))  # True
print(monotonic([4, 3, 2, 1]))  # True
```

This script defines a function `monotonic` that checks if the elements of the input list are monotonically increasing or decreasing. It does this by checking if all adjacent pairs of elements in the list satisfy the condition for monotonicity. If all pairs satisfy the condition, the function returns `True`; otherwise, it returns `False`. The test cases at the end of the script demonstrate the function's behavior on different inputs.