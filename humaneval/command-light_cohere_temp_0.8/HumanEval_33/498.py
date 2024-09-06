```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 7, 11])
    [11, 10, 7, 2]
    >>> sort_third([4, 12, 8, 6, 9])
    [6, 9, 8, 12]
    """
    return sorted(lst, key=lambda x: int(x) // 3 if int(x) % 3 == 0 else x)
```