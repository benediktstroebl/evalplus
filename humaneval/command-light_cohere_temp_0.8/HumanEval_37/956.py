```python
def sort_even(l: list):
    """Sorts list l such that values at even indices are sorted as equal to values at the even indices of the original list, and the rest remains in order.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l.sort_even(l)
    return l
```