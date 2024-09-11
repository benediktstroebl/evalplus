```python
def incr_list(lst: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        lst (list): A list of numbers.

    Returns:
        list: The input list with each element incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in lst]


if __name__ == "__main__":
    print(incr_list([1, 2, 3]))
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `incr_list` that takes a list of numbers as input and returns a new list with each element incremented by 1. It uses a list comprehension to achieve this. The docstring explains the purpose of the function, its arguments, and its return value. The example use cases demonstrate how to use the function.