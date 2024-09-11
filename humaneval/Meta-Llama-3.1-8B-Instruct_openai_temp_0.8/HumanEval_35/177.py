```python
def max_element(l: list) -> int:
    """Return maximum element in the list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:
        raise ValueError("List is empty")
    return max(l)

# Test cases
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

This script uses Python's built-in `max` function to find the maximum element in a list. If the list is empty, it raises a `ValueError`.