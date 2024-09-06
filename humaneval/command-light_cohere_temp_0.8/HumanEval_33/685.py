```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 6, 9, 15, 2, 3, 8, 5, 7])
    [2, 6, 3, 8, 5, 7, 9, 10]
    >>> sort_third([4, 9, 2, 7, 8, 10, 6, 5, 3])
    [2, 4, 6, 7, 8, 9, 10, 5, 3]
    """
    l = sorted(l, key=lambda x: int(x) // 3 if int(x) % 3 == 0 else int(x) // 3)
    return l
```