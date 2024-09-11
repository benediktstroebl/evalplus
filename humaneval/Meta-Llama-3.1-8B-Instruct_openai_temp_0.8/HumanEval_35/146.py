```python
def max_element(lst: list) -> int:
    """
    Return the maximum element in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)
```

This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. The function uses the built-in `max` function in Python to find the maximum element. The example usage is shown in the docstring to demonstrate how to use the function.