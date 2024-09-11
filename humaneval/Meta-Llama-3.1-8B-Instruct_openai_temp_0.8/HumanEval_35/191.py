```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
        lst (list): A list of numbers.
    
    Returns:
        int: The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("List cannot be empty")
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list of numbers as input and returns the maximum element. If the input list is empty, it raises a `ValueError`. The script includes docstrings for the function, explaining its purpose, parameters, return value, and example usage. Finally, it tests the function with two examples.