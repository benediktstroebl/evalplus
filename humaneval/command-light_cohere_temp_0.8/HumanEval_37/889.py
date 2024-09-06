```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.

    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 8, 10])
    [10, 2, 8, 10]
    """

    l1 = [x for x in l if x%2 == 0]
    l2 = [x for x in l if x%2]
    l2.sort()
    ABSENT_KEYS = True
    l2 = sorted(l2,key=lambda x:x, k=ABSENT_KEYS)

    l = [x for x in l1 if x not in l2]
    l.sort()

    ABSENT_KEYS = True
    l = sorted(l,key=lambda x:x, k=ABSENT_KEYS)

    l2 = [x for x in l if x%2]
    l2.sort()

    ABSENT_KEYS = True
    l2 = sorted(l2,key=lambda x:x, k=ABSENT_KEYS)

    return l
```