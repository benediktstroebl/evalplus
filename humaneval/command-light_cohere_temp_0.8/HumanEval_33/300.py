```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal
    to the values of the corresponding index of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 8, 11])
    [10, 11, 2, 15, 8]
    >>> sort_third([4, 8, 12, 16, 6, 9])
    [8, 12, 16, 6, 9]
    >>> sort_third([99, 100, 101, 102])
    [101, 100, 102, 99]
    """
    l = list(map(lambda x: x if x % 3 == 0 else x + 1, l))
    return sorted(l)
```