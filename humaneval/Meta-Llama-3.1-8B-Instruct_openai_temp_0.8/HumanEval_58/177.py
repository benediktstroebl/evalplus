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
    return sorted(set(l1) & set(l2))


# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

This script defines the `common` function, which takes two lists as input and returns a sorted list of unique elements that are common to both lists. The function uses the `set` data structure to find the intersection of the two lists, which effectively gives us the common elements. The result is then sorted using the `sorted` function and returned. The example usage at the end demonstrates how to use the `common` function with the provided test cases.