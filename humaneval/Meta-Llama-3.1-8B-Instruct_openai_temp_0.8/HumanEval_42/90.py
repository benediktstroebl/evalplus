```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
    l (list): A list of integers

    Returns:
    list: A list of integers where each element is incremented by 1

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Test the function
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This Python script defines a function `incr_list` that takes a list of integers as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to efficiently create the new list. The script also includes docstrings and example usage to demonstrate how to use the function.