```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list, sort it, and return it
    return sorted(list(common_elements))

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script solves the problem by first converting the input lists to sets, which automatically removes any duplicate elements. It then finds the intersection of the two sets using the `&` operator, which returns a set of elements that are common to both sets. Finally, it converts this set back to a list, sorts it, and returns it. The result is a sorted list of unique common elements from the two input lists.