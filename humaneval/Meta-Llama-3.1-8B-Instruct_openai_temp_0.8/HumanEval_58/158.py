### Common Elements in Two Lists
#### Problem Description
This script takes two lists as input and returns the sorted unique common elements.

#### Solution

```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set back to a list, sort it, and return it
    return sorted(list(common_elements))

# Example usage
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script uses the `set` data structure to remove duplicates and improve lookup efficiency. The `&` operator is used to find the intersection of the two sets, which gives us the common elements. The result is converted back to a list, sorted, and returned.