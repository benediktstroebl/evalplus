```python
def incr_list(lst: list) -> list:
    """
    Return a list with elements incremented by 1.

    Args:
        lst (list): A list of integers.

    Returns:
        list: The list with each element incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in lst]


# Test the function
if __name__ == "__main__":
    print(incr_list([1, 2, 3]))
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `incr_list` that takes a list of integers as input and returns a new list with each element incremented by 1. The `if __name__ == "__main__":` block is used to test the function with the provided example inputs.