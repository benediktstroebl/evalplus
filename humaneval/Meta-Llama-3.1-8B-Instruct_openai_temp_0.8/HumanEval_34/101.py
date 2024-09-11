```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
        l (list): The input list
    
    Returns:
        list: A sorted list of unique elements
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input, converts it to a set to remove duplicates, and then sorts the resulting set to return a sorted list of unique elements. The function is then tested with the example provided in the docstring.