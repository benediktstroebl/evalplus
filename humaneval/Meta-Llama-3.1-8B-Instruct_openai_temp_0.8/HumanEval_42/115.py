```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.
    
    Args:
    l (list): The input list.
    
    Returns:
    list: The list with elements incremented by 1.
    
    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]

# Test the function
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. It uses a list comprehension to achieve this in a concise and efficient way. The function also includes docstrings with examples to provide a clear understanding of its usage and behavior. The script then tests the function with the provided examples to demonstrate its correctness.