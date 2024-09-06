```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding index of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 20, 30, 40, 50, 60, 70, 80])
    [40, 50, 60, 70, 80, 10, 20, 30]
    """
    l = list(range(0, len(l), 3))
    l.sort(key=lambda x: not (x%3 == 0))
    return l
```