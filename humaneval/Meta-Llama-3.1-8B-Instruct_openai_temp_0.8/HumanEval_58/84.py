```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list of elements.
        l2 (list): The second list of elements.

    Returns:
        list: A sorted list of unique common elements.

    Example:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    return sorted(set(l1) & set(l2))

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script uses Python's built-in `set` data structure to find the intersection of the two lists, which represents the common elements. The `sorted` function is then used to sort the elements in ascending order. The `&` operator is used to find the intersection of the two sets. 

Note that this solution assumes that the elements in the lists are hashable, meaning they can be added to a set. If the lists contain unhashable elements (like lists or dictionaries), a different approach would be needed.