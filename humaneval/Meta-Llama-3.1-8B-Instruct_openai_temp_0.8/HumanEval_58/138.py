```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets, which gives the common elements
    common_elements = set1.intersection(set2)
    
    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Example usage
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

In this script, we use Python's built-in `set` data structure to efficiently find the common elements between the two lists. We convert the lists to sets using the `set()` function, find the intersection of the two sets using the `intersection()` method, and then convert the resulting set back to a list and sort it using the `sorted()` function. The sorted list of unique common elements is then returned.