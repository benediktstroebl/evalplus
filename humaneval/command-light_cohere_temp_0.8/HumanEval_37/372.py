```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 1, 2])
    [10, 1, 2]
    >>> sort_even([10, 1, 2], [100, 200])
    [10, 100, 200]
    """
    l.sort_even([1, 2, 3])
    assert len(l) == 3
    assert l[0] == 1 and l[1] == 2 and l[2] == 3
    assert l[1] == l[2] and l[0] == l[3]
    assert l[3] == 5 and l[2] == 6 and l[1] == 4
    assert l[0] != l[1] and l[0] != l[2] and l[1] != l[3]
    assert l[3] != l[2] and l[3] != l[1]
```