```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

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

In this script, we define a function `common` that takes two lists `l1` and `l2` as input. We convert each list to a set (which removes duplicates and allows for efficient set operations), find their intersection using the `&` operator, and then convert the result back to a list and sort it using the `sorted` function. The result is a list of unique common elements from the input lists, sorted in ascending order.