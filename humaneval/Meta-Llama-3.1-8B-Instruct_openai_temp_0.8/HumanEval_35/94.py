```python
def max_element(lst: list) -> any:
    """
    Return maximum element in the list.

    Args:
        lst (list): Input list.

    Returns:
        any: Maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("Cannot find maximum element in an empty list")
    return max(lst)
```

This script defines a function `max_element` that takes a list as input and returns the maximum element in the list. It uses the built-in `max` function to achieve this. It also includes a check to handle the edge case where the input list is empty. If the list is empty, it raises a `ValueError` with a descriptive error message.