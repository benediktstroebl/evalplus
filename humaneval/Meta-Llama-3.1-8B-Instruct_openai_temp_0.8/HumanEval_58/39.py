```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    s1 = set(l1)
    s2 = set(l2)
    
    # Find the intersection of the two sets
    common_elements = s1.intersection(s2)
    
    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
```

This script defines a function `common` that takes two lists as input, removes duplicates, finds the common elements using the `intersection` method of sets, and returns the result as a sorted list. The example usage demonstrates how to call the `common` function with two lists and print the resulting common elements.