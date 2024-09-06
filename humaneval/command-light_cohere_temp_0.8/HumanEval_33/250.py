```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical
    to l in the indic that are not divisible by three, while its values at the indic
    that are divisible by three are equal to the values of the corresponding indic
    of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 3, 20, 4])
    [20, 3, 10, 4]
    >>> sort_third([7, 8, 15, 16, 4])
    [4, 7, 8, 15, 16]
    """
    lst = sorted(lst, key=lambda x: x // 3)
    lst = [x for x in lst if x % 3 == 0]
    return lst
```