```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]

    """return sorted([x for x in l if x % 3 == 0], reverse=True) + [l[i] for i in range(len(l)) if l[i] % 3]
```  This function takes a list l and returns a new sorted list l', where the values at indices that are divisible by three are equal to the corresponding values in l, but the values at indices that are not divisible by three are sorted in ascending order.