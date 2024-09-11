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
    # Check if the list is not empty
    if not l:
        raise ValueError("List is empty")

    # Use built-in max function to find the maximum element
    return max(l)
```

This script uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. If the list is empty, it raises a `ValueError` because the maximum element of an empty list is undefined.