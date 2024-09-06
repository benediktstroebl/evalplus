```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 3, 7])
    [10, 2, 3, 7, 15]
    >>> sort_third([4, 9, 12, 11, 10, 8])
    [4, 9, 11, 10, 8]
    """
    l = list(map(lambda x: x if x % 3 == 0 else x + 1, l))
    return sorted(l)
```