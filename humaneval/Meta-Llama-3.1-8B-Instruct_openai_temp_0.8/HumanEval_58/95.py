```python
def common(l1: list, l2: list) -> list:
    """
    Return sorted unique common elements for two lists.

    Args:
        l1 (list): The first list.
        l2 (list): The second list.

    Returns:
        list: A sorted list of unique common elements.

    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    # Convert lists to sets for efficient lookup and intersection
    set1 = set(l1)
    set2 = set(l2)

    # Find the intersection of the two sets
    common_elements = set1.intersection(set2)

    # Convert the set back to a list and sort it
    common_elements = sorted(list(common_elements))

    return common_elements
```

This script defines a function `common` that takes two lists `l1` and `l2` as input, finds the common elements by converting them to sets and using the `intersection` method, and returns the common elements as a sorted list. The script also includes docstrings and example use cases to provide a clear understanding of the function's behavior.