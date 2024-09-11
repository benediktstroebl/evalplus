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
    common_elements = set1.intersection(set2)
    
    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))
    
    return common_elements

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines the `common` function, which takes two lists as input and returns a sorted list of unique common elements. The function uses Python's built-in `set` data structure to efficiently find the common elements and remove duplicates. The result is then sorted and returned as a list. The example usage at the end demonstrates how to use the `common` function with the provided test cases.