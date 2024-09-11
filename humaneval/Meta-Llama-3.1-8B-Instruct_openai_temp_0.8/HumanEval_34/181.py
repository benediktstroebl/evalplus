```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
    l (list): A list of elements.
    
    Returns:
    list: A sorted list of unique elements.
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates, and then convert it back to a list
    unique_list = list(set(l))
    
    # Sort the list in ascending order
    unique_list.sort()
    
    return unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set and back to a list, and then sorts the list in ascending order. The function is then tested with the provided example.