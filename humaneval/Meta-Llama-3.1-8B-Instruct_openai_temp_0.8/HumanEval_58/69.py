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
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (i.e., common elements)
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    common_list = sorted(list(common_elements))

    return common_list

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
# Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))
# Output: [2, 3]
```

This script uses Python's built-in set data type to efficiently find the intersection (common elements) of the two input lists, removing duplicates in the process. The result is then converted back to a list, sorted in ascending order, and returned.