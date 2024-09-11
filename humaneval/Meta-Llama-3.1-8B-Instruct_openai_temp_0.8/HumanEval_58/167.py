```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2
    
    # Convert the set back to a list, sort it and return
    return sorted(list(common_elements))


# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a `common` function that takes two lists as input and returns a new list containing the sorted unique elements that are common to both lists. The function uses set operations to find the intersection of the two lists, which is more efficient than checking each element individually. The result is then sorted and returned as a list. The test cases provided in the docstring are included at the end of the script to verify the function's correctness.