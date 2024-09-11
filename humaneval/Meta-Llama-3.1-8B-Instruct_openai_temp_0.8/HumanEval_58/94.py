```python
def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists."""
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    s1 = set(l1)
    s2 = set(l2)
    
    # Find the intersection of the two sets, which gives the common elements
    common_elements = s1 & s2
    
    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements


# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script uses Python's built-in `set` data type to efficiently find the common elements between two lists. It first converts the lists to sets, then uses the `&` operator to find their intersection, and finally converts the result back to a list and sorts it. The sorted list of common elements is then returned by the function.