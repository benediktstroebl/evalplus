```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.
    
    Args:
    l (list): The input list of numbers.
    
    Returns:
    list: The list with elements incremented by 1.
    
    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Example usage:
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script uses a list comprehension to create a new list where each element is the corresponding element in the input list plus one. The function is well-documented with a docstring that includes examples of how to use the function.