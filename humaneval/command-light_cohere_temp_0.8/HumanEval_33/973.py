```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal to the values of the corresponding index of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 20, 40, 19, 19, 34, 35, 67, 19])
    [10, 1, 19, 19, 19, 34, 35, 67, 20, 67, 40]
    >>> sort_third([10, 1, 2, 20, 40, 19, 19, 34, 35, 67, 19, 70])
    [10, 19, 19, 19, 34, 35, 67, 67, 70, 20, 67]
    """
    lst = sorted(lst, key=lambda x: int(x / 3) % 3)
    return lst
```