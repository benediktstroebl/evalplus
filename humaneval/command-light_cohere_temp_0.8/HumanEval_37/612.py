```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indic are equal
    to the values of the even indic of l, but sorted.
    >>> sorted(list([1, 2, 3])) == sort_even([1, 2, 3])
    True
    >>> sorted(list([5, 6, 3, 4])) == sort_even([3, 6, 5, 4])
    True
    """
    l = l.sortind(key=lambda x: not x%2)
    l.sortind(key=lambda x: x)
    l = list(l)
    return l
```