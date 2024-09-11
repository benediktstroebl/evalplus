```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): First list to find common elements in.
        l2 (list): Second list to find common elements in.

    Returns:
        list: Sorted list of unique common elements.

    Example:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    return sorted(set(l1) & set(l2))

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This Python script defines a function `common` that takes two lists as input and returns their sorted unique common elements. It uses the set intersection operator `&` to find common elements and then converts the resulting set back to a list, removes duplicates, and sorts it.