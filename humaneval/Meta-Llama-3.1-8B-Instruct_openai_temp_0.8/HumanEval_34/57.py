```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_elements = set(l)
    
    # Convert the set back to a list and sort it
    sorted_unique_elements = sorted(list(unique_elements))
    
    return sorted_unique_elements

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and then sorts the set to produce a list of unique elements in sorted order. The function is then tested with the example provided.