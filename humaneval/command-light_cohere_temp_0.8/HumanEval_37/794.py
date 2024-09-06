```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.

    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 4, 8])
    [4, 8, 10, 2]
    >>> sort_even([1, 10, 5, 9])
    [9, 10, 1, 5]
    """
    l = sorted([[x, y] for x, y in l if y % 2 == 0])
    return [item for sublist in l for item in sublist]
```