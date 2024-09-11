```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l (list): A list of elements.
    
    Returns:
        The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if len(l) == 0:
        return None  # or raise an exception, depending on the requirements
    
    return max(l)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script defines a function `max_element` that takes a list `l` as input and returns its maximum element. If the list is empty, it returns `None` (you can also raise an exception if required). The function uses Python's built-in `max` function to find the maximum element.