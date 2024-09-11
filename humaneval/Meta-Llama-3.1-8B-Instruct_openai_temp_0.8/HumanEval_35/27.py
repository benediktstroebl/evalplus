```python
def max_element(lst: list) -> int:
    """
    Return the maximum element in the list.

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

This script defines a function `max_element` that takes a list of integers and returns the maximum element in the list. It uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments.

Note: I changed the function parameter name to `lst` for clarity, and also changed the return type annotation to `int`.