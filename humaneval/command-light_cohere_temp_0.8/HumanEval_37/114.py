```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index,
    while its values at the even index are equal to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Build a new list l' such that l[0] is kept as it is, and l[1:] is kept sorted
    l' = [x for x in l if x%2 != 0] + [l[1]]
    return l'
```