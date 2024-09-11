```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
        l (list): A list of elements.
    
    Returns:
        list: A list of unique elements in sorted order.
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates, then convert it back to a list
    # and sort it in ascending order
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as an argument, removes duplicates by converting the list to a set, and then sorts the unique elements in ascending order before returning them as a list. The function is then tested with the provided example.