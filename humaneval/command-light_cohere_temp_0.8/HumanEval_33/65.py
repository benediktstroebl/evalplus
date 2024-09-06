```python
def sort_third(l: list):
    """Sorts list l such that the values divisible by three are sorted first, then all other values are sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 6, 2, 8, 1, 3])
    [1, 2, 6, 8, 3, 10]
    """
    l.sort_third = [list](sort(l[l.find_all(3, l)])
    l.sort_third = [list](l.sort(l[l.find_all(3, l)))
    return l.sort_third

    ```
    Example usage:
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    ```