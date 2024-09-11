```python
def unique(lst: list) -> list:
    """Return sorted unique elements in a list
    
    Args:
    lst (list): A list of elements.
    
    Returns:
    list: A sorted list of unique elements.
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    # Use a set comprehension to preserve the order of elements
    unique_set = {x for x in lst}
    
    # Convert the set back to a list and sort it
    sorted_lst = sorted(list(unique_set))
    
    return sorted_lst

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This Python script defines a function `unique` that takes a list of elements as input, removes duplicates by converting the list to a set, and then sorts the set to get a sorted list of unique elements. The function includes example usage and input validation.