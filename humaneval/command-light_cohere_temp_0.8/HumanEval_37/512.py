```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 20, 30, 10, 40])
    [10, 20, 30, 40]
    >>> sort_even([5, 6, 3, 4, 5])
    [3, 6, 5, 4]
    >>> sort_even([4, 6, 7, 8])
    [4, 6, 7, 8]
    """
    l = sorted(l)
    return l
```