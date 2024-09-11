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
    return max(l)

# Test the function
print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

This script defines a function `max_element` that takes a list `l` as input and returns its maximum element using the built-in `max` function. The function also includes docstrings to provide documentation and examples of its usage. The script then tests the function with the provided examples.