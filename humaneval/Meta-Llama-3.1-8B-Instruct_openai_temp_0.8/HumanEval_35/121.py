```python
def max_element(lst: list) -> int:
    """
    Return the maximum element in the list.
    
    Args:
        lst (list): The list to find the maximum element in.
    
    Returns:
        int: The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

Note that the built-in `max()` function in Python is used to find the maximum element in a list. This function is more efficient and readable than implementing a custom solution.