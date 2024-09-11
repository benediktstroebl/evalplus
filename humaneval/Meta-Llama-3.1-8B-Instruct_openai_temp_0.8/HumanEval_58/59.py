```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_set = set1 & set2
    
    # Convert the set back to a list, sort it, and return it
    return sorted(list(common_set))

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script defines the `common` function, which takes two lists as input, finds their common elements by taking the intersection of the two lists converted to sets, removes duplicates, sorts the common elements, and returns them. The test cases at the end demonstrate the function's usage and expected output.