```python
def unique(lst: list):
    """Return sorted unique elements in a list.
    
    Args:
        lst (list): A list of elements.
    
    Returns:
        list: A sorted list of unique elements.
    
    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))


# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `unique` that takes a list as input, removes duplicates by converting it to a set, and returns a sorted list of unique elements. The `sorted` function is used to sort the elements in ascending order. The script also includes a test case to demonstrate the function's usage.