```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 10, 20, 30])
    [10, 10, 20, 30]
    >>> sort_even([1, 2, 3, 4, 5])
    [1, 2, 3, 4]
    >>> sort_even([0, 2, 3, 100, 7])
    [0, 2, 3, 100]
    """
    l = [0, 2, 3, 4, 5]
    l.sort(key=lambda x: x % 2 == 0)
    l.extend(0, 2, 3, 4, 5)
    return l
```