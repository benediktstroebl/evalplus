```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 6, 18, 9])
    [10, 2, 6, 18, 9, 15]
    >>> sort_third([1, 2, 2, 3, 3])
    [1, 2, 2, 3, 3]
    """
    l = sorted(l, key=lambda x: x // 3 if x % 3 == 0 else x)
    return l
```