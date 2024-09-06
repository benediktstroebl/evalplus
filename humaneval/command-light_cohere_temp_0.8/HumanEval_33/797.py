```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the third
    position, while its values at positions [0, 1, 2] are equal to the values of the corresponding positions in l, but sorted.
    >>> sort_third([1, 2, 3])
    [3, 1, 2]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 8, 7, 18, 10, 14, 13, 12])
    [10, 2, 15, 8, 13, 10, 14, 18, 10, 12, 7]
    """
    l[:2] = [x for x in l[0:2]] + [x for x in l[2:]]
    l[2:] = [x for x in l[2:][::-1]] + [x for x in l[0:2]]
    return l
```