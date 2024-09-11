```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list and sort it
    common_list = sorted(list(common_elements))
    
    return common_list

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script defines a function `common` that takes two lists as input, finds their common elements, removes duplicates, and returns the common elements in sorted order. The script also includes test cases to demonstrate the function's correctness.