```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    third, while its values at indices that are divisible by three are sorted.

    >>> sort_third([1, 2, 3])
    [3, 1, 2]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_copy = l[:] + [x if i%3 == 0 else x-3 for i, x in enumerate(l)] + l[-1:]
    return l_copy
```