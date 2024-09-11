```python
def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists."""
    
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list and sort it
    result = sorted(list(common_elements))
    
    return result

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# [2, 3]
```

This script defines a function `common` that takes two lists as input and returns a list of sorted unique common elements. It uses Python's built-in set data structure to efficiently find the common elements and improve performance. The test cases demonstrate the function's correctness.