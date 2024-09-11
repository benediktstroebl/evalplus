### Increment List Elements by 1
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
    l (list): A list of numbers.

    Returns:
    list: The input list with each element incremented by 1.

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```
This function uses a list comprehension to create a new list where each element is the corresponding element in the input list incremented by 1. The function takes a list of numbers as input and returns the incremented list.