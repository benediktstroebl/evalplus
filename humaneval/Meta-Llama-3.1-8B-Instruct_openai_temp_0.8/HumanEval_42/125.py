```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list of numbers.

    Returns:
        list: The list with all elements incremented by 1.

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

This Python script defines a function `incr_list` that takes a list of numbers as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to achieve this in a concise and efficient way. The script also includes docstrings to provide documentation and test cases to demonstrate the function's behavior.