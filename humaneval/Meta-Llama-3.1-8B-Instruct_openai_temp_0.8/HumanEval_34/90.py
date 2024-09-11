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
    # Use set to remove duplicates and convert back to list
    unique_list = list(set(l))
    
    # Sort the list in ascending order
    unique_list.sort()
    
    return unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function called `unique` that takes a list of elements as input, removes duplicates by converting the list to a set, and then sorts the set in ascending order before returning it.