```python
def sort_even(lst):
    """This function sorts a list l such that the elements at odd positions are kept as they are, and the elements at even positions are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    return lst[:] + [x if x % 2 == 0 else x[::-1] for x in lst[1:]]
```