```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): A list of integers.

    Returns:
        list: A new list with elements incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]
```

This script defines a function `incr_list` that takes a list of integers as input and returns a new list with each element incremented by 1. It uses a list comprehension to achieve this in a concise and efficient manner.