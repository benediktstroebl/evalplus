```python
def sort_third(l: list):
    """Sorts list l such that values divisible by three appear at indices that are divisible by three, while other values are ordered.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = [x for x in l if x % 3 != 0] + [x for x in l if x % 3 == 0]
    return sorted(l)
```