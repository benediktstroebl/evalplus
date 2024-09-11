```python
def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists."""
    
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2
    
    # Convert the intersection back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines a function `common` that takes two lists as input, finds their common elements, removes duplicates, sorts the common elements, and returns them as a list. The function uses a set to efficiently find the intersection of the two lists, and it uses the `sorted` function to sort the common elements. The script includes docstrings and test cases to demonstrate the function's usage and behavior.