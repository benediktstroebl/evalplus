```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    >>> sorted(range(10), interval=2, reverse=False)
    [8, 6, 4, 2, 0, 10, 9]
    """
    l.insert(0, 0)
    return list(l)
```