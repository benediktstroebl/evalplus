```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.
    
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: Sorted unique common elements.
    """
    # Convert lists to sets for efficient lookup
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2
    
    # Convert the set back to a list and sort it
    common_list = sorted(list(common_elements))
    
    return common_list


# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script defines a function `common` that takes two lists as input, finds their common elements, and returns them in sorted order. The function uses sets for efficient lookup and conversion between lists and sets. The example usage demonstrates the function's behavior with two different pairs of input lists.