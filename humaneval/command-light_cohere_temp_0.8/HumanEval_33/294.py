```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 99])
    [99, 11, 22, 33]
    """
    l = list(l)
    n = len(l)
    l_mod3 = [i for i in l if i % 3 == 0]
    l_equiv = [i for i in l if i == l[i]]
    l_equiv.sort(key=lambda x: x)
    l_equiv = [x for x in l_equiv]
    l = [x for x in l_equiv if x not in l_mod3]
    return l
```