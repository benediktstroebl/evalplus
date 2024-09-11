```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of elements.
    
    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    
    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return all(i <= j for i, j in zip(l, l[1:])) or all(i >= j for i, j in zip(l, l[1:]))

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list as input and returns `True` if the list elements are monotonically increasing or decreasing, and `False` otherwise. The function uses the `all` function and a generator expression to check if all pairs of adjacent elements in the list satisfy the condition of being either increasing or decreasing. The script also includes test cases to verify the correctness of the `monotonic` function.