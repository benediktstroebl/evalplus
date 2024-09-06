```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the indices that are divisible by three are equal to the values of the corresponding index of l, but sorted.

    Test suite:
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    l = [1, 2, 3]
    l.sort(key=lambda x: not x%3)
    l = l[::-1]
    return l
```