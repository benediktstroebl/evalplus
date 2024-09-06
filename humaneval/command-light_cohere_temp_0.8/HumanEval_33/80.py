```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 1, 8, 9, 6, 5])
    [1, 2, 8, 9, 6, 5, 10]
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l = sorted(l)
    l = l[:] + [x if x % 3 == 0 else x - 1  for x in l[1:]] + l[-1:]
    return l
```