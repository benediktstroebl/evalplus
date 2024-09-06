```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd indic,
    while its values at the even indices are equal to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 4, 8])
    [8, 10, 2, 4]
    """
    l.insert(0, 0)
    l.extend(1, -1)
    l.remove(0)
    l.sort()
    fact = l.count("1") > 0
    value in the odd index
    for i in range(1, len(l)):
        if l.count("1") > 0:
            l[i] = l[i-1]
    return l
```