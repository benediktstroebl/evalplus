```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of integers.

    Returns:
        list: List with elements incremented by 1.

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

This script defines a function `incr_list` that takes a list of integers as input, increments each element by 1, and returns the resulting list. The function uses a list comprehension to efficiently create the new list. The script also includes docstrings and test cases to demonstrate the function's usage.