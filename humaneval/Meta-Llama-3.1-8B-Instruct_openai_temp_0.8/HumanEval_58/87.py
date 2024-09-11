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
    # Convert the lists to sets to remove duplicates and have an O(1) lookup time
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (i.e., the common elements)
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists as input, removes duplicates by converting them to sets, finds the intersection of the two sets to get the common elements, and then converts the result back to a list and sorts it. The function is then tested with the provided example inputs.