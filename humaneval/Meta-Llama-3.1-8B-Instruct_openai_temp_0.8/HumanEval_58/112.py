```python
def common(l1: list, l2: list) -> list:
    """Return sorted unique common elements for two lists."""
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

In this script, we define a function `common` that takes two lists `l1` and `l2` as input. We convert these lists to sets (which automatically removes duplicates) and then find their intersection using the `&` operator. The intersection of two sets is a new set that contains only the elements that are common to both sets. We then convert this set back to a list and sort it before returning it. The function includes docstrings to explain its behavior and several test cases to demonstrate its correctness.