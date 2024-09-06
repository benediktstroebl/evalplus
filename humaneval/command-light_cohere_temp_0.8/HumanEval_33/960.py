```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the values at indices that are not
    divisible by three are in l' are the same as the values at the corresponding indices in l, but are sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    lst[:] = [x for x in lst if x % 3 != 0]
    return lst
```