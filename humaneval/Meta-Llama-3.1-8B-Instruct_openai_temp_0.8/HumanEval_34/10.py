```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
    l (list): Input list of elements.
    
    Returns:
    list: Sorted list of unique elements from the input list.
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script works by first converting the input list to a set, which removes any duplicate elements. The `set` data structure in Python is an unordered collection of unique elements. Then it converts this set back to a list, sorts it in ascending order using the `sorted` function, and returns the result.