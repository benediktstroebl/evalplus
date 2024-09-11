### Common Elements in Two Lists
#### Python Script

```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list of elements.
        l2 (list): The second list of elements.

    Returns:
        list: A sorted list of unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    result = sorted(list(common_elements))

    return result

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script uses Python's built-in set data structure to efficiently find the common elements between two lists. It first converts the input lists to sets, then finds the intersection of the two sets (which gives the common elements), and finally converts the set of common elements back to a list and sorts it. The result is a sorted list of unique common elements.