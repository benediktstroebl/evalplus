### Common Elements in Two Lists
```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): First list to find common elements in.
        l2 (list): Second list to find common elements in.

    Returns:
        list: Sorted list of unique common elements.

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
In this script, we define the `common` function that takes two lists as input. It first converts each list to a set (which automatically removes duplicates), then uses the `&` operator to find the intersection of the two sets (i.e., the common elements). Finally, it sorts the resulting set and returns it as a list. The example usage demonstrates how to call the function with different inputs.