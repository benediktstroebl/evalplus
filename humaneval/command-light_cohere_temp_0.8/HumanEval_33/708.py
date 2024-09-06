```python
def sort_third(lst):
    """This function sorts a list l such that all the values divisible by three appear in their correct order.
    >>> sort_third([1, 2, 3])
    [1, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 8, 6, 9, 5])
    [2, 8, 6, 9, 5, 10]
    """
    l = []
    for x in lst:
        if x % 3 == 0:
            l.append(x(x))
    else:
        l.append(x(x))
    l.sort()
    all for i in range(3, len(l)):
        l[i] = l[i] + l[i-3]
    return l
```