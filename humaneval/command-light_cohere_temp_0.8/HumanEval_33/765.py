```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the items that are not divisible by three, while its values at the items divisible by three are equal to the values of the corresponding items of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 6, 4, 8, 3, 5, 7])
    [2, 6, 4, 8, 3, 5, 7]
    """
    lst = list(map(lambda x: x if x % 3 != 0 else x, lst))
    return sorted(lst)
```