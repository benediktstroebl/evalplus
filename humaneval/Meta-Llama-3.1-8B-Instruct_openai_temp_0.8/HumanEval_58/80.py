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
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_set = set1.intersection(set2)
    
    # Convert the set back to a list, sort it, and return it
    return sorted(list(common_set))

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script uses Python's built-in `set` data structure to efficiently find the common elements between the two lists. It first converts the lists to sets to remove duplicates and improve lookup efficiency, then finds the intersection of the two sets using the `intersection` method. Finally, it converts the resulting set back to a list, sorts it, and returns it.