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
    return sorted(set(l1) & set(l2))

# Test the function
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines a function `common` that takes two lists as input and returns a sorted list of unique elements that are common to both lists. The function uses Python's built-in `set` data type to find the intersection of the two sets of elements, and then converts the resulting set back to a sorted list using the `sorted` function. The test cases are included to demonstrate the function's behavior.