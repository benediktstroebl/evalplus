```python
def common(l1: list, l2: list):
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements.

    Example:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Convert lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (common elements)
    common_elements = set1 & set2

    # Convert the set back to a list and sort it
    common_list = sorted(list(common_elements))

    return common_list

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

In this script, we define a function `common` that takes two lists `l1` and `l2` as input. It first converts these lists to sets to remove duplicates and improve lookup efficiency. The intersection of the two sets is then calculated using the `&` operator to find the common elements. Finally, the common elements are converted back to a list, sorted, and returned.

The script also includes example use cases to demonstrate the function's behavior.