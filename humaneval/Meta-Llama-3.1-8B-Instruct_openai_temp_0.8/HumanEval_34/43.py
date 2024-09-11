```python
def unique(l: list):
    """Return sorted unique elements in a list
    Args:
    l (list): Input list of elements
    Returns:
    list: Sorted list of unique elements
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, the `unique` function uses a combination of the `set` data structure and the `sorted` function to return a sorted list of unique elements. The `set` data structure automatically removes duplicates, and the `sorted` function sorts the resulting set in ascending order. This approach has a time complexity of O(n log n) due to the sorting operation, where n is the number of unique elements in the list.