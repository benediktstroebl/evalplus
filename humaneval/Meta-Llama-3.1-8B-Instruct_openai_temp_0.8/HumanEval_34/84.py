```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates, then convert back to a list
    unique_list = list(set(l))
    
    # Sort the list in ascending order
    sorted_list = sorted(unique_list)
    
    return sorted_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting the list to a set, and then sorts the resulting set in ascending order. The function is then tested with a sample input list.