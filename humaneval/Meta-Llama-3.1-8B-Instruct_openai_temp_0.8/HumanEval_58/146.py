```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets to get common elements
    common_elements = set1 & set2
    
    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Expected output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Expected output: [2, 3]
```

This script defines a function `common` that takes two lists as arguments, finds their common elements (ignoring duplicates), and returns the result as a sorted list. The function uses Python's built-in `set` data type for efficient lookup and merge operations. The test cases at the end of the script demonstrate the function's correctness.