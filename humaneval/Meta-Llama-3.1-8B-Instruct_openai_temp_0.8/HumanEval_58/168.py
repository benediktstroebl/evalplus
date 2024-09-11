Here is the Python script that solves the problem in a markdown code block:

### Common Elements in Two Lists
#### Description
This script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements.

#### Code
```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.
    
    Args:
    l1 (list): The first list.
    l2 (list): The second list.
    
    Returns:
    list: A sorted list of unique common elements.
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]

print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

#### Explanation
The `common` function uses set operations to efficiently find the common elements between two lists. It first converts the lists to sets, which allows for fast lookup and removal of duplicates. The `&` operator is used to find the intersection of the two sets, which gives the common elements. Finally, the set of common elements is converted back to a list and sorted before being returned.