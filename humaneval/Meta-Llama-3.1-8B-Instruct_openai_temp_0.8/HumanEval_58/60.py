```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., elements common to both lists)
    common_elements = set1.intersection(set2)
    
    # Convert the set of common elements back to a list and sort it
    sorted_common_elements = sorted(list(common_elements))
    
    return sorted_common_elements

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script uses Python's built-in `set` data structure to efficiently find the intersection of the two input lists, which represents the elements common to both lists. The resulting intersection is then converted back to a list and sorted before being returned. 

This approach ensures that the output is a sorted list of unique common elements, as required by the problem statement.