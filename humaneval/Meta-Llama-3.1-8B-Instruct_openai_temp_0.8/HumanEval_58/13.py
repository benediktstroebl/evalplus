**Common Elements in Two Lists**
================================

Here's a Python script that defines a function `common` to find and return sorted unique common elements for two lists:

```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements.

    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find common elements by taking the intersection of the two sets
    common_elements = set1 & set2

    # Convert the set of common elements back to a list and sort it
    common_list = sorted(list(common_elements))

    return common_list

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

In this script, the `common` function first converts the input lists to sets to remove duplicates and improve lookup efficiency. It then finds the common elements by taking the intersection of the two sets. Finally, it converts the set of common elements back to a list, sorts it, and returns the result. The script includes example usage at the end to demonstrate how to use the `common` function.