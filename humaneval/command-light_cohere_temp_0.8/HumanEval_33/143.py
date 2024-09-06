```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 45, 67, 90])
    [45, 90, 13, 67, 67, 67, 67, 67, 67, 67, 90, 10, 2]
    """
    l.sort_third(l)
```

The function called sort_third in this code takes a list l as input and returns a new list l'. The function sorts the values in l that are divisible by three to their correct positions, and the remaining values are sorted normally.