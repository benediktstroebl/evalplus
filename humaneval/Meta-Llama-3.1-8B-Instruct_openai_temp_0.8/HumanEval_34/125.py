```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    # and then convert it back to a list
    unique_elements = list(set(l))
    
    # Sort the list in ascending order
    unique_elements.sort()
    
    return unique_elements

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script first removes all duplicate elements from the input list by converting it to a set, then converts it back to a list. It then sorts the list in ascending order using the built-in `sort` method. The resulting list is then returned by the function.