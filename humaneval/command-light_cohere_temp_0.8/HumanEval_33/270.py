```python
def sort_third(lst):
    """
    The function takes a list l as input and returns a list l' such that
    l' contains values at indices not divisible by three from l,
    in sorted order.
    """
    test the wrapped as a list comprehension and sorting using sorted(). plain list
    lst[:] = sorted(lst[:])
    lst = lst[3:]
    return lst
```