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
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1.intersection(set2)
    
    # Convert the set of common elements back to a list and sort it
    common_list = sorted(list(common_elements))
    
    return common_list

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements. The function first converts the lists to sets to remove duplicates and improve lookup efficiency. It then finds the intersection of the two sets (i.e., the common elements) using the `intersection` method. Finally, it converts the set of common elements back to a list, sorts it, and returns it. The script includes two test cases to demonstrate the function's behavior.