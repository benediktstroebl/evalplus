```python
def sort_even(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([11, 22, 33, 44])
    [11, 22, 33, 44]
    >>> sort_even([1, 2, 33, 3, 4])
    [3, 2, 33, 4]
    """
    lst[1], lst[2] = lst[2], lst[1]
    return lst
```