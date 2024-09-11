```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    l (list): The list to find the maximum element from.
    
    Returns:
    The maximum element in the list.
    
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if len(l) == 0:
        raise ValueError("Cannot find maximum of an empty list")
    return max(l)

# Test the function
print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

This Python script uses the built-in `max()` function to find the maximum element in the list. If the list is empty, it raises a `ValueError`. The script includes docstrings for the function and provides example usage.