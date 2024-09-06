```python
def sort_even(lst):
    """Sorts a list l such that all odd indexes have their elements, and all even indexes have equal values with elements from l, sorted.
    >>> sorted(list(range(10)), reverse=True)
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> sort_even([9, 8, 7, 6])
    [9, 8, 7]
    >>> sort_even([5, 6, 7, 8])
    [8, 5, 6]
    >>> sort_even([3, 8, 7, 4, 5, 6])
    [4, 5, 8, 7]
    >>> sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    l = [9, 8, 7, 6]
    for i in range(len(l)):
        if l[i] % 2 == 1:
            l[i], l[i+1] = l[i+1], l[i]
    else:
        l[i], l[i+1] = l[i+1], l[i]
    return l
```