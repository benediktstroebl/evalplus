```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.
    
    Args:
        l1 (list): The first list.
        l2 (list): The second list.
    
    Returns:
        list: A sorted list of unique common elements.
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Use set intersection to find common elements
    common_elements = set1 & set2
    
    # Convert the set back to a list and sort it
    common_list = sorted(list(common_elements))
    
    return common_list

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script uses Python's built-in `set` data structure to remove duplicates and improve lookup efficiency. The `&` operator is used to find the intersection of two sets, which represents the common elements. The result is then converted back to a list and sorted before being returned.