```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.

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

# Test cases
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

Note: The built-in `max()` function in Python already returns the maximum element in a list, so the `max_element()` function is essentially redundant. However, it can be useful for educational purposes or when the `max()` function is not available.