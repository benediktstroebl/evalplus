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
    # Convert the list to a set to remove duplicates
    # Convert the set back to a list and sort it
    return sorted(list(set(l)))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then sorts the unique elements in ascending order. The example usage at the end demonstrates how to use the function.