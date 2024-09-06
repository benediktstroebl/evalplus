```python
def sort_third(l: list):
    """Sorts list l such that values not divisible by three remain unchanged, and the rest are sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l[:] = [x for x in l if x % 3 != 0]
    return list(sorted(l))
```