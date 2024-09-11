```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., common elements)
    common_set = set1.intersection(set2)
    
    # Convert the set back to a list and sort it
    common_list = sorted(list(common_set))
    
    return common_list


# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

In this script, we use Python's built-in `set` data type to efficiently find the common elements between two lists. The `intersection` method returns a new set containing only the elements that are present in both sets. We then convert this set back to a list, sort it, and return the result.