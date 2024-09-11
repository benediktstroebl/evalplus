```python
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list of elements.
        l2 (list): The second list of elements.

    Returns:
        list: A sorted list of unique common elements.
    """
    # Convert the lists to sets to eliminate duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets, which are the common elements
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines a function `common` that takes two lists `l1` and `l2` as input, finds their common elements, eliminates duplicates, and returns the common elements in sorted order. The function uses Python's built-in `set` data structure to improve lookup efficiency and eliminate duplicates. The test cases at the end demonstrate the function's correctness.