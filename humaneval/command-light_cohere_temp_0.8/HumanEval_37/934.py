```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.
    >>> sorted(list([1, 2, 3]))
    [1, 2, 3]
    >>> sorted(list([5, 6, 3, 4]))
    [3, 6, 5, 4]
    """
    l.append(0)
    for i in range(len(l)//2):
        l[i], l[i+len(l)//2] = l[i+len(l)//2], l[i]
    return l
```