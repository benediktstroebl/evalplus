```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the indices that are divisible by three are equal to the values of the corresponding index of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 20, 30,40, 50, 60])
    [50, 60, 40, 30, 20, 10]
    """
    l = list(map(lambda x: x if x % 3 == 0 else x+1, l))
    return l
```