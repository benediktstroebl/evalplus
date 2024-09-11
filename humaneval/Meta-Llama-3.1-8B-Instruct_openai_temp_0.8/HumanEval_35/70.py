```python
def max_element(lst: list):
    """Return maximum element in the list.
    
    Args:
    lst (list): A list of elements.
    
    Returns:
    The maximum element in the list.
    
    Raises:
    ValueError: If the list is empty.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:
        raise ValueError("Cannot find maximum of an empty list")
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that returns the maximum element in a list. It uses the built-in `max` function to find the maximum element. If the list is empty, it raises a `ValueError`. The script also includes example use cases to demonstrate how to use the function.