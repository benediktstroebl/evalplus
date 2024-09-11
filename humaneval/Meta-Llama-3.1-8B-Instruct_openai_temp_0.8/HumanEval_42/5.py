```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): A list of elements to be incremented.

    Returns:
        list: A new list with elements incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]
```

This script defines a function `incr_list` that takes a list `l` as input, increments each element in the list by 1, and returns the resulting list. The increment operation is performed using a list comprehension, which is a concise and readable way to create a new list by applying a transformation to each element of an input list. 

You can test this function by calling it with a list of numbers, like this: `print(incr_list([1, 2, 3]))`.