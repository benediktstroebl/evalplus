### Find Maximum Element in a List
```python
def max_element(lst: list) -> int:
    """
    Returns the maximum element in the list.

    Args:
    lst (list): List of elements.

    Returns:
    int: Maximum element in the list.

    Example:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)


# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Raises ValueError: List is empty
```

Note: This script uses the built-in `max` function in Python to find the maximum element. The `max` function returns the largest item in an iterable or the largest of two or more arguments.