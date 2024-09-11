```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): The input list.

    Returns:
        list: A sorted list of unique elements.

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script uses the built-in `set` function to remove duplicates and then sorts the resulting set using the `sorted` function. The `sorted` function returns a new sorted list and leaves the original set unchanged.