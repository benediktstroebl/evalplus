```python
def max_element(l: list) -> int:
    """Return maximum element in the list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script uses the built-in `max()` function in Python to find the maximum element in the list. The `max()` function returns the largest item in an iterable or the largest of two or more arguments.