```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and have efficient lookup
    s1 = set(l1)
    s2 = set(l2)
    
    # Find the intersection of the two sets (i.e., common elements)
    common_elements = s1 & s2
    
    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines the `common` function as specified and includes two test cases at the end to demonstrate its usage. The function works by first converting the input lists to sets, which are unordered collections of unique elements that support efficient lookup. It then finds the intersection of the two sets (i.e., the common elements) using the `&` operator, converts the result back to a list, and sorts it before returning it.