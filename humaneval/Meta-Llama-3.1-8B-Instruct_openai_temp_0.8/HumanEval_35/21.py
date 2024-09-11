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
    if not l:
        raise ValueError("List cannot be empty")
    return max(l)

# Test cases
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
print(max_element([]))  # Expected output: Raises ValueError
```

This script defines a function `max_element` that returns the maximum element in a given list `l`. It uses the built-in `max` function in Python to find the maximum element. The script also includes test cases to demonstrate the function's behavior. If the input list is empty, the function raises a `ValueError` as per the problem's requirements.