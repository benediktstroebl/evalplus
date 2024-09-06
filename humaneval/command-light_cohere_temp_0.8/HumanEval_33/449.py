```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 6, 99])
    [15, 6, 10, 2, 99]
    >>> sort_third([1, 2, 3, 6, 9])
    [9, 6, 3, 2]
    >>> sort_third([10, 13, 21, 18, 5, 6, 99])
    [99, 18, 21, 10, 6, 5]
    """
    l.sort(l[:len(l)//3] + [x for x in l[len(l)//3:]]
    return l
```