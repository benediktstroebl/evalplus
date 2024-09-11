```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of numbers.

    Returns:
        list: List of numbers incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```

This script defines a function `incr_list` that takes a list of numbers `l` and returns a new list where each number is incremented by 1. The function uses a list comprehension to achieve this in a concise and efficient manner. The example use cases are included in the docstring for clarity and testing purposes.