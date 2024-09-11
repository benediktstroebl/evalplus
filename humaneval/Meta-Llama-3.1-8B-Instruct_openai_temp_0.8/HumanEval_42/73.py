```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The list to be incremented.

    Returns:
        list: The incremented list.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Example usage:
print(incr_list([1, 2, 3])) 
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This Python script defines a function `incr_list` that takes a list as input and returns a new list with each element incremented by 1. The function uses a list comprehension to create the new list. The example usage demonstrates the function's behavior with two different input lists.