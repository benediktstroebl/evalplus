```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 4, 8])
    [8, 10, 2, 4]
    """
    l = l.sort()
    odd = []
    for i in range(len(l)):
        if l[i] % 2 == 1:
            odd.append(l[i])
    else:
            even.append(l[i])
    l = odd + even
    return l
```