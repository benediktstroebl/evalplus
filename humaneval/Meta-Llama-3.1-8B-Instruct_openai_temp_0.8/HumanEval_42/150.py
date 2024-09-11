```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.
    
    Args:
    l (list): A list of integers.
    
    Returns:
    list: The input list with each element incremented by 1.
    
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

This script defines a function `incr_list` that uses a list comprehension to return a new list where each element is the corresponding element from the input list incremented by 1. The function is then demonstrated with example usage.