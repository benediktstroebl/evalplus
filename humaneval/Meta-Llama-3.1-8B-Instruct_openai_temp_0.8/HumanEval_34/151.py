```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    
    Args:
        lst (list): Input list
    
    Returns:
        list: List of unique elements in sorted order
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Convert list to a set to remove duplicates, then convert back to a list
    unique_lst = list(set(lst))
    
    # Sort the list in ascending order
    unique_lst.sort()
    
    return unique_lst

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set and back to a list, and then sorts the list in ascending order. The function includes a docstring that explains its purpose, parameters, return value, and provides an example use case.