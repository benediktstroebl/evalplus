```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    s1 = set(l1)
    s2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = s1.intersection(s2)
    
    # Convert the result back to a list and sort it
    result = sorted(list(common_elements))
    
    return result

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script defines the `common` function to find the sorted unique common elements in two lists. It first converts the lists to sets to remove duplicates and improve lookup efficiency. It then finds the intersection of the two sets (i.e., the common elements) using the `intersection` method. Finally, it converts the result back to a list, sorts it, and returns it. The test cases at the end demonstrate how to use the function.