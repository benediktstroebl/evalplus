```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
    l (list): A list of elements
    
    Returns:
    list: A sorted list of unique elements
    
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then sorts the unique elements in ascending order before returning them. The test case at the end demonstrates how the function can be used.