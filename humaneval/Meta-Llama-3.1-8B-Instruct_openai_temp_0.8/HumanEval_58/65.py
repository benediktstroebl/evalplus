```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
    l1 (list): The first list of elements.
    l2 (list): The second list of elements.

    Returns:
    list: A sorted list of unique elements common to both input lists.

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
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    common_list = sorted(list(common_elements))

    return common_list

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input, removes duplicates by converting them to sets, finds the intersection of the two sets to identify common elements, and returns a sorted list of these common elements. The function includes docstrings for documentation and example usage to demonstrate its functionality.