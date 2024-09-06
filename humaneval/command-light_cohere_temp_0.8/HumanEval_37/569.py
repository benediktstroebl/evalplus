```python
def sort_even(lst):
    """This function sorts the list lst such that the elements at odd indices are kept as they are, and the elements at even indices are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    lst = lst.sort(reverse)
    # extract even indices
    idx = [i for i,x in enumerate(lst) if x%2 == 0]
    lst = [x for i,x in enumerate(lst) if i in idx]
    return lst
```