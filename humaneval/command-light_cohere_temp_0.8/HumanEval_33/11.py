```python
def sort_third(lst):
    """Sorts the list l such that values at indices divisible by three are sorted to the front, and the rest are sorted to the back.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 3, 6, 1, 4])
    [1, 2, 3, 6, 10]
    >>> sort_third([10, 2, 3, 6, 1, 4, 7, 5])
    [1, 2, 3, 6, 7, 5, 4, 10]
    """
    return lst[:int(len(lst) / 3):] + lst[int(len(lst) / 3):int(len(lst) / 3 * 2):]
```