```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2
    
    # Convert the set back to a list, sort it, and return it
    return sorted(list(common_elements))

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script defines a function `common` that takes two lists as input, finds their common elements, removes duplicates, and returns the result in sorted order. The `set` data structure is used for efficient lookup and intersection operations. The `sorted` function is used to sort the common elements in ascending order before returning them.