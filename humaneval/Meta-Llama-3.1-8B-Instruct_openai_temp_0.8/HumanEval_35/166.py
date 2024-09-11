```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): The input list.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, we use the built-in `max()` function in Python to find the maximum element in the list. This approach is simple and efficient, as it avoids the need to implement a custom comparison function.