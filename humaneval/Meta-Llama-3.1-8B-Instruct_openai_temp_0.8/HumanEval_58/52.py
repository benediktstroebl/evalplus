```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., elements common to both)
    common_elements = set1 & set2
    
    # Convert the result back to a list and sort it
    result = sorted(list(common_elements))
    
    return result

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script defines a function `common` that takes two lists as input, finds their common elements, removes duplicates, sorts the result, and returns it. It then tests this function with two example inputs, demonstrating its correctness.