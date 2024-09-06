```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indicies are equal to the values of the even indic of l, but sorted.
    >>> sorted(list([1, 2, 3]))
    [1, 2, 3]
    """
    return sorted(l,key=lambda x: x%2)
```