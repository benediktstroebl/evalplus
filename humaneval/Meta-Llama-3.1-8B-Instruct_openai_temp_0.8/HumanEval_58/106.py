```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements.
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of the two sets, which are the common elements
    common_set = set1.intersection(set2)
    
    # Convert the set back to a list and sort it
    common_list = sorted(list(common_set))
    
    return common_list

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements. It uses Python's built-in `set` data structure to efficiently find the intersection of the two lists. The `intersection` method returns a new set with elements common to both sets. The result is then converted back to a list, sorted, and returned. The script includes two test cases to demonstrate the function's correctness.