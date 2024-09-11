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
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets
    common_elements = set1.intersection(set2)
    
    # Convert the set back to a list and sort it
    result = sorted(list(common_elements))
    
    return result

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input, finds the unique common elements, and returns them in sorted order. It uses sets to improve lookup efficiency and convert the lists to sets using the `set` function, finds the intersection of the two sets using the `intersection` method, converts the set back to a list using the `list` function, and sorts the list using the `sorted` function. The function is then tested with the provided example use cases.