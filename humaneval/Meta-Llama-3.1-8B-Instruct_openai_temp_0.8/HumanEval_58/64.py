```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): First list of elements.
        l2 (list): Second list of elements.

    Returns:
        list: Sorted unique common elements.

    Example:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    return sorted(set(l1) & set(l2))

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script uses Python's built-in `set` data structure to find the intersection of two lists (i.e., their common elements). The `&` operator is used to compute the set intersection. The `sorted` function is then used to sort the resulting list of common elements in ascending order.