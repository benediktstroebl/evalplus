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
    # Convert lists to sets for efficient lookup and removal of duplicates
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = set1.intersection(set2)

    # Convert the set back to a list, sort it, and return
    return sorted(list(common_elements))

# Test cases
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script uses the built-in `set` data structure in Python, which provides efficient lookup and removal of duplicates. The `intersection` method is used to find the common elements between the two sets, and the result is converted back to a list, sorted, and returned. The test cases at the end demonstrate the function's behavior.