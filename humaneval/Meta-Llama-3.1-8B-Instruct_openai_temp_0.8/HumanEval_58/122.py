```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

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
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2
    
    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input, finds their common elements, removes duplicates, sorts the result, and returns the list of common elements. The function uses sets to efficiently find common elements and remove duplicates. The script also includes test cases to demonstrate the function's correct behavior.