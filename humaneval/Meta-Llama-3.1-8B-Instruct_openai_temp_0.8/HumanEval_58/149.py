```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): First list of elements.
        l2 (list): Second list of elements.

    Returns:
        list: Sorted list of unique common elements.

    Example:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find common elements using set intersection
    common_elements = set1 & set2

    # Convert set back to list and sort it
    sorted_common_elements = sorted(list(common_elements))

    return sorted_common_elements

# Example usage
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

In this script, we first convert the input lists to sets to remove duplicates and improve lookup efficiency. We then use the `&` operator to find the common elements between the two sets. Finally, we convert the resulting set back to a list, sort it, and return the result.