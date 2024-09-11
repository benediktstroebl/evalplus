```python
def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if list elements are monotonically increasing or decreasing, False otherwise.
    
    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if list is empty
    if len(l) == 0:
        return True
    
    # Check if list is monotonically increasing
    increasing = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    
    # Check if list is monotonically decreasing
    decreasing = all(l[i] >= l[i + 1] for i in range(len(l) - 1))
    
    # Return True if list is either monotonically increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
print(monotonic([]))  # Expected output: True
print(monotonic([5]))  # Expected output: True
```

In this code, we first check if the list is empty. If it is, we return True, as an empty list can be considered as monotonically increasing or decreasing. Then we check if the list is monotonically increasing or decreasing using the `all()` function and generator expressions. The `or` operator is used to return True if the list is either monotonically increasing or decreasing.