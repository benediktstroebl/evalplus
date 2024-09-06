```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the indices that are divisible by three are equal to the values of the corresponding index of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 16, 3, 6, 7, 8, 9])
    [10, 2, 3, 6, 8, 9, 15, 16, 7]
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    divisible = [i for i,j in enumerate(l) if j%3 == 0]
    for i in range(len(l)):
        if i not in divisible:
            l[i] = l[len(l)-1]
    l = sorted(l)
    return l
```