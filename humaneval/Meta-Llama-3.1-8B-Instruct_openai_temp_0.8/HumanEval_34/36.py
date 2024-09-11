```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
    l (list): A list of elements
    
    Returns:
    list: A sorted list of unique elements
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    unique_set = set(l)
    
    # Convert the set back to a list and sort it
    unique_list = sorted(list(unique_set))
    
    return unique_list

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

However, a more concise solution using Python's built-in `sorted` function with the `set` data structure would look like this:

```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
    l (list): A list of elements
    
    Returns:
    list: A sorted list of unique elements
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```