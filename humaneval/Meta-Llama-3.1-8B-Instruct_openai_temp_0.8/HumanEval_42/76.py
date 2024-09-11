```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
    l (list): Input list.

    Returns:
    list: List with elements incremented by 1.

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # Use a list comprehension to create a new list where each element is the input list's element incremented by 1
    return [x + 1 for x in l]

# Test the function with some examples
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the function `incr_list` uses a list comprehension to create a new list where each element is the input list's element incremented by 1. This is a concise and efficient way to create a new list based on an existing list. The script also includes some example usage of the function and prints the results to the console.