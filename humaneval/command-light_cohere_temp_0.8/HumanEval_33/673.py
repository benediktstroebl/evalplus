```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    third position, while its values at positions 1 and 2 are sorted.
    >>> sort_third([1, 2, 3])
    [1, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 3, 1])
    [1, 3, 10]
    """
    l.sort(l[:2], l[(2+1):])
```