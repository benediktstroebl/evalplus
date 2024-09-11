```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        The maximum element in the list.

    Raises:
        ValueError: If the list is empty.

    Examples:
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
```

This script defines a function `max_element` that takes a list as input and returns its maximum element. The function uses Python's built-in `max` function, which returns the largest item in an iterable. If the input list is empty, it raises a `ValueError`. The example usage at the end demonstrates how to use the `max_element` function with different inputs.