```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
    l (list): A list of numbers.

    Returns:
    list: A new list with all elements incremented by 1.

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]
```

In this script, we define a function `incr_list` that takes a list of numbers as input and returns a new list where each number has been incremented by 1. The function uses a list comprehension to create the new list. This is a concise and efficient way to perform the increment operation on all elements of the input list.