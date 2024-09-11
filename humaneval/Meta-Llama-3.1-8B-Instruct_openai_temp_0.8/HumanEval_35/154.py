```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): A list of elements.

    Returns:
        The maximum element in the list.

    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

This script defines a function `max_element` that takes a list as input and returns the maximum element in the list. It uses Python's built-in `max` function to find the maximum element.

The script also includes docstrings to explain what the function does, its arguments and return values, and provides examples of how to use it. Finally, it tests the function with the examples provided in the problem statement.