```python
def max_element(lst: list) -> int:
    """
    Return maximum element in the list.

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
    if not lst:
        raise ValueError("List is empty")

    return max(lst)
```

In this code:

1.  We define a function `max_element` that takes a list of integers as input.
2.  We check if the list is empty and raise a `ValueError` if it is.
3.  We use the built-in `max` function to find the maximum element in the list.
4.  We include docstrings to provide documentation for the function, including its parameters, return values, and examples of usage.