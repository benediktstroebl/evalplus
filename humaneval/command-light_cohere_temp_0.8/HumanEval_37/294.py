```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    """
    list(l)
    if len(l) % 2 == 0:
        l.sort(key=lambda x: not x % 2)
    else:
        l.sort(key=lambda x: x % 2)
    return l
```