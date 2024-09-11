```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set back to a list and sort it
    common_list = sorted(list(common_elements))
    
    return common_list

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input, finds their common elements (ignoring duplicates), and returns these elements in sorted order. It uses Python's set data structure to efficiently find the common elements. The script also includes test cases to verify the function's correctness.