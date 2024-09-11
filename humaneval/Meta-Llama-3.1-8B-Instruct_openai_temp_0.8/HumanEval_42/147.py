```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The list of integers to be incremented.

    Returns:
        list: The incremented list.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]

# Testing the function
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the `incr_list` function uses a list comprehension to create a new list with each element incremented by 1. The function then returns this new list.