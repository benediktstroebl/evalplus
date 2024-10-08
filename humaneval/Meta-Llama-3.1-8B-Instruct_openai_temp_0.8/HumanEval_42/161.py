```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.
    
    Args:
        l (list): The input list of integers.
    
    Returns:
        list: The input list with elements incremented by 1.
    
    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]
```

This function uses a list comprehension to create a new list where each element is the previous element plus one. It takes advantage of Python's immutable nature by avoiding modifying the original list.