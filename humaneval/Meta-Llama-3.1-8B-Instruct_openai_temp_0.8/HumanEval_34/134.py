```python
def unique(lst: list):
    """Return sorted unique elements in a list
    
    Args:
    lst (list): A list of elements.
    
    Returns:
    list: A sorted list of unique elements.
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, converts it into a set to remove duplicates, and then sorts the resulting set before returning it. The `set` data structure in Python is a collection of unique elements, and the `sorted` function is used to sort the elements in ascending order.