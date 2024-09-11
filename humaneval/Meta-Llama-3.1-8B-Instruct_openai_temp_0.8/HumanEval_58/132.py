**Common Elements in Two Lists**
================================

The following Python script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements.

```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = set1.intersection(set2)

    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements

# Example use cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists `l1` and `l2` as input. It converts these lists to sets to remove duplicates and improve lookup efficiency. The intersection of the two sets is then found using the `intersection` method, which returns a new set containing the common elements. Finally, the set of common elements is converted back to a list, sorted in ascending order, and returned.