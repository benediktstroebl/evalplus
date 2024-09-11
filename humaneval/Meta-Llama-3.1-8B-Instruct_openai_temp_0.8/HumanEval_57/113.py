```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    Args:
        l: A list of numbers.
    
    Returns:
        A boolean indicating whether list elements are monotonically increasing or decreasing.
    
    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    # First element can be any value
    # Check if all subsequent elements are greater than the previous one
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    
    # Check if all subsequent elements are less than the previous one
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    
    # Return True if list is either increasing or decreasing
    return increasing or decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements of a list are monotonically increasing or decreasing. The function uses the `all` function with a generator expression to check if all elements after the first one are greater than or less than the previous one. The function returns `True` if the list is either increasing or decreasing, and `False` otherwise.