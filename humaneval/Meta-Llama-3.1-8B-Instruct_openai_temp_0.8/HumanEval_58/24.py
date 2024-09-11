### Sorted Unique Common Elements in Two Lists
#### Problem Description
This script finds the sorted unique common elements between two input lists.

#### Solution
```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    s1 = set(l1)
    s2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = s1 & s2
    
    # Convert the set of common elements back to a list, sort it, and return it
    return sorted(list(common_elements))


# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script uses Python's built-in set data type to efficiently find the common elements between the two input lists. The `&` operator is used to find the intersection of the two sets, which gives us the common elements. Finally, the script converts the set of common elements back to a list, sorts it, and returns it.