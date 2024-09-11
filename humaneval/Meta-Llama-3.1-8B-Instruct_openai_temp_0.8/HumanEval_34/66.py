```python
def unique(lst: list) -> list:
    """
    Return sorted unique elements in a list.
    
    Args:
        lst (list): The input list.
    
    Returns:
        list: A sorted list of unique elements.
    
    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(lst))  # Convert to set (removes duplicates), then sort

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the `unique` function works by converting the input list to a set, which automatically removes any duplicate elements. It then sorts the resulting set and returns it. This approach is more efficient than trying to sort the original list and then removing duplicates, as it avoids the unnecessary work of comparing and sorting elements that will be removed anyway.