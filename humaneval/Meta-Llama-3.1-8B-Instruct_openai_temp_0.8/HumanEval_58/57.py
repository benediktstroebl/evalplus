```python
def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists."""
    
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_set = set1 & set2
    
    # Convert the set back to a list, sort it, and return it
    common_list = sorted(list(common_set))
    
    return common_list

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines a function `common` that takes two lists as input, finds their common elements, removes duplicates, sorts the result, and returns it. The function uses Python's built-in `set` data structure to efficiently find common elements and remove duplicates. The test cases demonstrate the function's behavior with different input lists.