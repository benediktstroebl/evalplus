```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.

    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 8, 20])
    [10, 8, 2, 20]
    """
    l = [3, 6, 5, 4]
    return l[:-sort_even(l[1:])][::-1].index(l[0])] + l[1:]
```
The function sorts a list so that the odd index values are the same and the even index values are the same. The values at the  are sorted using the sort_even function and are returned in reverse order.