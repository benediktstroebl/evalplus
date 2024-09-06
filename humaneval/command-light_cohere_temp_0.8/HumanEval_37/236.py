```python
def sort_even(lst):
    """Sorts a list l such that all the odd index values are retained, and the even indices are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([11, 22, 33, 44])
    [11, 22, 33, 44]
    """
    return sorted(lst, key=lambda x: x % 2)
```