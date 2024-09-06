```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 13, 33, 99])
    [33, 99, 10, 13, 2]
    >>> sort_third([0, 2, 2, 2])
    [2, 2, 2, 2]
    """
    l1 = []
    for i in l:
        if i % 3 == 0:
            l1.append(i)
   
    else:
            l1.append(i)
   
    l = l1
    l.sort()
    for i in l:
        print(i, end=' ')
    return l
```