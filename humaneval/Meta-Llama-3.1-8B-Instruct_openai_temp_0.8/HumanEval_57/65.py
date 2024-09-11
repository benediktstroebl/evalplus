```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
        l (list): The list to check for monotonicity.
    
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
    return all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

This script defines a function `monotonic` that takes a list `l` as input and returns `True` if the elements are monotonically increasing or decreasing, and `False` otherwise. The function uses two generator expressions within the `all` function to check for both increasing and decreasing monotonicity.