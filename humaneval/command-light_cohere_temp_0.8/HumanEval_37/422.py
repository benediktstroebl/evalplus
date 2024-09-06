```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sorted(range(10))
    [0, 3, 6, 9, 2, 4, 8, 1, 5]
    """
    l[:] = [x+1 for x in range(len(l))]
    l = sorted(l)
    return l
```