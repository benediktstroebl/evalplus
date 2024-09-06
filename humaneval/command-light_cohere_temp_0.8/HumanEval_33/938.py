```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 22, 11])
    [10, 13, 11, 22]
    >>> sort_third([10, 30, 20, 15])
    [10, 15]
    """
    l = [10, 20, 30, 22, 11]
    l.sort_by_third(l)
    return [x for x in l if x not in l.sort_by_third(l)]
```

This script defines a function called `sort_third` that sorts a list `l` such that the values at indices that are not divisible by three are kept as they are, while the values at indices that are divisible by three are equal to the corresponding values of `l`, but are sorted.

The `sort_third` function then sorts the list `l` using the `sort_by_third` function and returns a new list `l'` where the values at indices that are not divisible by three are kept as they are, and the values at indices that are divisible by three are equal to the corresponding values of `l`, but are sorted.