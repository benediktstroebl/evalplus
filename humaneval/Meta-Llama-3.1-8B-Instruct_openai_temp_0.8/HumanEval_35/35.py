```python
def max_element(lst: list) -> int:
    """
    Return maximum element in the list.

    Args:
        lst (list): The list to find the maximum element from.

    Returns:
        int: The maximum element in the list.

    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

This script defines a function `max_element` that takes a list as input and returns its maximum element. The function uses the built-in `max` function in Python to find the maximum element. The example usage is provided in the docstring and also tested in the script.