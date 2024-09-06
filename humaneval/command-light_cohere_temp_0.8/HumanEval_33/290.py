```python
def sort_third(lst):
    """This function sorts the list l such that elements not divisible by three stay in their original order, and the rest are sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 6, 9, 1, 8])
    [1, 2, 6, 8, 9, 10]
    >>> sort_third([25, 26, 39, 36, 45, 32, 50, 58])
    [26, 39, 36, 45, 32, 50, 58, 25]
    >>> sort_third([1, 2, 3, 9, 9, 10, 20, 90])
    [1, 2, 3, 9, 9, 10, 20, 90]
    """
    l = sorted(lst, key=lambda x: int(x) % 3 == 0)
    return l
```