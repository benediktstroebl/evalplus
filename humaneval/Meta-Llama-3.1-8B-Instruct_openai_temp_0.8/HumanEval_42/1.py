```python
def incr_list(lst: list) -> list:
    """Return list with elements incremented by 1.

    Args:
        lst (list): The input list.

    Returns:
        list: The list with all elements incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in lst]
```

This script defines a function `incr_list` that takes a list as an argument and returns a new list where all elements are incremented by 1. It uses a list comprehension to achieve this in a concise and efficient way.