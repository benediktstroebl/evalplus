```python
def sort_even(l: list):
    """Sorts a list l of integers into a list l' where values of even indices are kept as is, and odd indices are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l1 = []
    for i in l:
        if i%2 == 0:
            l1.append(i)
   
    l = l1
    return l
```