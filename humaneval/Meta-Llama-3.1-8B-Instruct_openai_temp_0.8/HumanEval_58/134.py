```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements from the input lists.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Use set intersection to find common elements, convert back to list and sort
    common_elements = sorted(list(set(l1) & set(l2)))
    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This Python script defines a function `common` that takes two lists `l1` and `l2` as input and returns a sorted list of unique common elements. It uses the `set` data structure to find the intersection of the two lists, which automatically eliminates duplicates. The result is then sorted and returned. The script includes docstrings with examples to demonstrate its usage.