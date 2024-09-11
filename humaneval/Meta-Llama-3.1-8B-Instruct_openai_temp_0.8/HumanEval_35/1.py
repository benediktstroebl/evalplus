```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.
    
    Args:
    lst (list): A list of numbers.
    
    Returns:
    int: The maximum number in the list.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("Cannot find maximum of an empty list")
    return max(lst)  # Return the maximum element in the list

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list of numbers as an argument and returns the maximum number in the list. It includes a check to ensure that the list is not empty, raising a `ValueError` if it is. The function uses Python's built-in `max` function to find the maximum element. The script also includes example use cases.