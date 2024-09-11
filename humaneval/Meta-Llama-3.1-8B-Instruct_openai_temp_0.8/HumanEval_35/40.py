```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l (list): The input list of elements.
    
    Returns:
        The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    # Check if the list is empty
    if not l:
        raise ValueError("Cannot find maximum element in an empty list")
    
    # Use Python's built-in max function to find the maximum element
    return max(l)
```

This script uses Python's built-in `max` function to find the maximum element in a list. If the list is empty, it raises a `ValueError`.