### Common Elements in Two Lists
#### Problem Description
This Python script finds and returns the sorted unique common elements in two input lists.

#### Code
```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.
    
    Args:
        l1 (list): The first list.
        l2 (list): The second list.
    
    Returns:
        list: A sorted list of unique common elements.
    """
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2
    
    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

#### Explanation
This script defines a function `common` that takes two lists `l1` and `l2` as input. It first converts these lists to sets, which automatically removes any duplicate elements and provides efficient lookup capabilities. The `&` operator is then used to find the intersection of the two sets, which gives us the common elements. The resulting set of common elements is converted back to a list and sorted before being returned as the output.