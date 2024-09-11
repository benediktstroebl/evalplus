```python
def max_element(lst: list) -> int:
    """
    Return maximum element in the list.

    Args:
    lst (list): A list of integers.

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
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

Note: In Python 3.x, the built-in `max()` function can be used to find the maximum element in a list. The `max_element()` function is a simple wrapper around this built-in function. If you're working with Python 2.x, you can modify the function to handle the `list` type explicitly.