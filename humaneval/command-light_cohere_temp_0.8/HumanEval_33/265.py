```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    """
    [ [1, 2, 3]
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 6, 2, 8, 9])
    [8, 6, 2]
    >>> sort_third([11, 8, 9, 10, 2, 3, 1])
    [1, 8, 9]
    """
    l_divisible = [x for x in l if x % 3 != 0]
    l_nondivisible = [x for x in l_divisible if x % 3 == 0]
    l_return = [x for x in l if x not in l_n] + [y for y in l_nivisible if y != l_divisible[0]]
    return l_return
```