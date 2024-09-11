```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
    l1 (list): The first list.
    l2 (list): The second list.

    Returns:
    list: Sorted unique common elements of both lists.
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = set1.intersection(set2)

    # Convert the result back to a list and sort it
    result = sorted(list(common_elements))

    return result

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines a function `common` that takes two lists as input, finds their common elements using sets, removes duplicates, sorts the result, and returns it. The function includes docstring comments to explain its purpose, parameters, and return value. The script also includes example usage to demonstrate how to use the function.