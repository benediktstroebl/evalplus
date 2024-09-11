```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        int: The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:
        raise ValueError("List cannot be empty")
    
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Outputs: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Outputs: 123
```

This script defines the `max_element` function, which takes a list as input and returns its maximum element. It uses Python's built-in `max` function to find the maximum element. If the input list is empty, it raises a `ValueError`.