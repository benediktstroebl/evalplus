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

# Example usage:
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])) 
print(common([5, 3, 2, 8], [3, 2]))
```

This script defines a function `common` that takes two lists `l1` and `l2`. It uses the `set` function to convert the lists into sets, which are unordered collections of unique elements. The `&` operator is used to find the intersection of the two sets, which is the set of elements common to both sets. Finally, the `sorted` function is used to convert the set of common elements back into a sorted list, which is then returned by the function.

The script also includes two example usage calls to demonstrate the function's behavior.