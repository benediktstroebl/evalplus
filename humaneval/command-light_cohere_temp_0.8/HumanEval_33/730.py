```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal to the values of the corresponding index of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 20, 4, 6, 8, 18])
    [4, 6, 8, 10, 18, 2, 20]
    >>> sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [4, 6, 7, 8, 9, 5, 3, 2, 1]
    """
    l_even = []
    l_odd = []
    for i in l:
        if i % 3 == 0:
            l_even.append(i)
        else:
            l_odd.append(i)
   
    return l_odd
```