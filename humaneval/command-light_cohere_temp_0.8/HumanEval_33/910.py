```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 20, 4])
    [20, 10, 4]
    >>> sort_third([4, 2, 8, 22, 10, 6, 7])
    [8, 22, 10, 6, 7, 2]
    """
    l_copy = list(l)
    l_copy_divisible = [x for x in l_copy if x % 3 == 0]
    l_copy_non_divisible = [x for x in l_copy if x % 3 != 0]
    l_final = l_copy_non_divisible + [x if x in l_copy_divisible else y for x, y in zip(l_copy_divisible, l_copy_non_divisible)]
    return l_final
```

This script defines a function sort_third that sorts a given list l such that values at indices that are divisible by 3 are kept as they are, and the rest are sorted.  The final list is identical to the sorted version of l but with values that are divisible by 3 set to the corresponding values in l.