```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
    l (list): The input list of numbers.

    Returns:
    list: A new list with elements incremented by 1.

    Example:
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

This script uses a list comprehension to create a new list where each element is incremented by 1. It takes advantage of the fact that the `+` operator can be used to add a number to each element in a list.