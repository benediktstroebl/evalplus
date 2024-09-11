```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): A list of numbers

    Returns:
        list: A list with elements incremented by 1

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Test the function
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list of numbers as input and returns a new list with each element incremented by 1. The function uses a list comprehension to achieve this. The script includes docstrings and test cases to demonstrate the function's behavior.