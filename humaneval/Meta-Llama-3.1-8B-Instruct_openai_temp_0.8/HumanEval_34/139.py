```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
    l (list): Input list
    
    Returns:
    list: Sorted list of unique elements
    
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list `l` as input, removes duplicates by converting it to a set, and then sorts the resulting set in ascending order before returning it as a list. The test at the end of the script shows how to use this function with the provided example list.