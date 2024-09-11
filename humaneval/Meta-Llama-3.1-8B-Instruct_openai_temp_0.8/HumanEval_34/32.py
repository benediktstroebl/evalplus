```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
        l (list): The input list containing elements to be made unique.
    
    Returns:
        list: A sorted list of unique elements from the input list.
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the `unique` function uses the built-in `set` function to remove duplicates from the input list. The `sorted` function is then used to sort the unique elements in ascending order. The result is returned as a sorted list of unique elements.