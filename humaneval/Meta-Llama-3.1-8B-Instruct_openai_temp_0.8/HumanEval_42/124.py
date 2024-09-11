```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of integers to increment.

    Returns:
        list: List of incremented integers.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]
```

This script defines a function `incr_list` that takes a list of integers and returns a new list with each element incremented by 1. It uses a list comprehension to create the new list, which is more efficient and concise than using a for loop. The function includes a docstring that explains its purpose, input and output, and provides examples of usage.