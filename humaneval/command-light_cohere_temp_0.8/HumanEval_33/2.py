```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the third item, while its values at the 
    other positions are equal to the values of the corresponding 
    items in l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    lst[::3] = sorted(lst[::3:])
    return lst
```