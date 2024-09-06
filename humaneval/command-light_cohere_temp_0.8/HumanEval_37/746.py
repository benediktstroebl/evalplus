```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 8, 20])
    [10, 2, 8, 20]
    >>> sort_even([3, 2, 20, 8])
    [2, 20, 8, 3]
    """
    l = [3, 2, 20, 8, 10, 5, 6]
    l = l[:] + [10, 8] + l[1:]
    l = [num for num in l if num % 2 == 0] + l[1::2]
    return l
```