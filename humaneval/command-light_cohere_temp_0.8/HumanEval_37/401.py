```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 22, 33, 24, 11])
    [11, 10, 22, 24]
    >>> sort_even([7, 2, 88, 8, 5])
    [5, 7, 2, 8]
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even, odd = [x for x in l if x % 2 == 0]
    l = even + odd
    return l
```