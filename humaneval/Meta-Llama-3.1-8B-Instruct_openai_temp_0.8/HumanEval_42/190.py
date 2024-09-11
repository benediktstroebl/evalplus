```python
def incr_list(lst: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        lst (list): List of numbers

    Returns:
        list: List of incremented numbers

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in lst]
```

You can run this script and test the function with the provided examples to see that it works as expected. 

You can also test it with your own list of numbers to see how it increments them. 

Note: The function uses a list comprehension to iterate over the input list and increment each element by 1. This is a concise and efficient way to achieve the desired result.