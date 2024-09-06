```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([11, 22, 33, 55, 66,77])
    [77, 66, 55, 44, 33, 22, 11]
    """
    l.sort(key=lambda x: not x%2)
    l.sort()

```