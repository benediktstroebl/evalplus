```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = [1, 2, 3]
    m = [5, 6, 3, 4, 8, 9, 2]
    l.sort(l, lst = lst[1:] + [lst[0]] + lst[2:])
    lst = l + lst
    return lst
```