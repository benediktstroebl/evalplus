```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in terms of third
    values that are divisible by three, while its values that are not divisible by three are sorted.
    >>> [1, 2, 3]
    [2, 3, 1, 4, 8, 9]
    >>> [5, 6, 3, 4, 8, 9, 2]
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = [1, 2, 3]
    l.sort_by_three() = l[:] + [x * 3 for x in l[1:] + l[2:]]
    l.sort_by_three() = l[:] + [x * 3 for x in l[1:] + l[2:]]
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort_by_third() = l[:] + [x * 3 for x in l[1:] + l[2:]]
    l.sort_by_three() = l[:] + [x * 3 for x in l[1:] + l[2]]
    return l
```