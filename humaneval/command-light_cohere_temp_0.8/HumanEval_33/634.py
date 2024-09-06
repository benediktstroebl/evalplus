```python
def sort_third(l: list):
    """Sorts a list l so that values at indices divisible by three are in their correct positions, the
    rest are unchanged.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l.sort_list(l, key=lambda x: x // 3)
```