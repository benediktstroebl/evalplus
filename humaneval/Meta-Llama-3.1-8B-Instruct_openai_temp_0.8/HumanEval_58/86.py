```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list of elements.
        l2 (list): The second list of elements.

    Returns:
        list: A list of sorted unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert both lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = set1.intersection(set2)
    
    # Convert the set back to a list and sort it
    common_list = sorted(list(common_elements))
    
    return common_list

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input and returns a list of their common elements, sorted in ascending order and without duplicates. The function uses sets to improve efficiency and then converts the result back to a list before returning it. The script also includes test cases to demonstrate the function's usage.