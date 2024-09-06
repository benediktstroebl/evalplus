```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 5, 6, 3])
    [3, 6, 5, 10]
    >>> sort_even([4, 8, 12, 16])
    [12, 8, 16, 4]
    """
    l = l.sort(reverse)
    l[::2] = l[1::2]
    l[1::2] = l[::2]
    return l
```