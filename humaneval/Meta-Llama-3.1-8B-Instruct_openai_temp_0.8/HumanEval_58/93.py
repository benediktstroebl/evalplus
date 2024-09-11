```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.

    :param l1: The first list.
    :param l2: The second list.
    :return: A sorted list of unique common elements.
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements. The function uses Python's set data type to efficiently find the common elements and then converts the result back to a list and sorts it. The script includes docstrings to document the function's behavior and examples to demonstrate its usage.