```python
def unique(l: list):
    """
    Return sorted unique elements in a list
    
    Args:
        l (list): The input list containing elements
    
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

This Python script defines a function `unique` that takes a list `l` as input, converts it to a set (which automatically removes duplicates), and then converts it back to a list before sorting it. The sorted list of unique elements is then returned.

When you run this script, it will print the sorted list of unique elements from the provided example list.