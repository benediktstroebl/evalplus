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

This Python script defines a function `max_element` that takes a list of integers as an input and returns the maximum element in the list. It uses the built-in `max` function in Python to find the maximum element. The function also includes a check for an empty input list and raises a `ValueError` in such cases.

Note that the time complexity of this function is O(n) where n is the length of the input list because the `max` function in Python needs to iterate over the entire list to find the maximum element.