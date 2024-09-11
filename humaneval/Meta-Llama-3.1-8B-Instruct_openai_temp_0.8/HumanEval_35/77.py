```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. It uses Python's built-in `max` function to find the maximum element. If the input list is empty, it raises a `ValueError`. The function includes docstrings to provide documentation and example usage.