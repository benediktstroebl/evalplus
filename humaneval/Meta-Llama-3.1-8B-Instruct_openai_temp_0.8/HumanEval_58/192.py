### Common Elements in Two Lists

This Python script defines a function `common` that takes two lists as input and returns a sorted list of unique common elements.

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
    # Convert the lists to sets to remove duplicates and improve lookup efficiency
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets (i.e., the common elements)
    common_set = set1.intersection(set2)

    # Convert the set back to a list, sort it, and return it
    return sorted(list(common_set))


# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

This script first converts the input lists to sets, which removes duplicates and improves the efficiency of the lookup operation. It then finds the intersection of the two sets, which gives the common elements. Finally, it converts the set back to a list, sorts it, and returns it. The test cases at the end demonstrate the function's behavior.