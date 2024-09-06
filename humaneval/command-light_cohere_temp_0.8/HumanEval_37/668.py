```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = [4, 7, 2, 1, 3,5,6]
    l = l1[:] + [6, 4, 7][::-1]
    l.sort()
    way = lambda x: x != x[0] and x[0] % 2 == 0
    return l[:::].index(lambda x: x.sort(lambda x: x == x[1:])) + l[1::]
```