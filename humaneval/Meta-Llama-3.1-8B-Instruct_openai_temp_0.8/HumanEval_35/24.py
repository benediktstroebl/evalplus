```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): Input list of elements.

    Returns:
        int or float: Maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)

# Example usage:
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, I've implemented the `max_element` function using Python's built-in `max` function, which returns the largest item in an iterable (such as a list).