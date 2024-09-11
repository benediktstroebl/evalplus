```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    
    # Convert lists to sets to remove duplicates and then find intersection
    common_elements = set(l1).intersection(set(l2))
    
    # Convert the set back to a list, sort it and return
    return sorted(list(common_elements))

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script defines a function `common` that takes two lists as input, finds their unique common elements by converting them to sets and finding their intersection, and returns these common elements sorted in ascending order. The function is then tested with the example use cases provided.