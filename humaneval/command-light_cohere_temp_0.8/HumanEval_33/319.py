```python
def sort_third(lst):
    """Returns a list l' such that l' is identical to l in the
    third decimal place, while its values at decimal places
    0, 1, and 2 are equal to the values of the corresponding
    indices of l, but sorted.

    >>> sorted_third([1, 2, 3])
    [1, 2, 3]
    >>> sorted_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sorted_third([10, 2, 6, 4, 8, 3, 1])
    [1, 2, 6, 4, 8, 3, 10]
    >>> sorted_third([1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    lst = [1, 2, 3, 4, 5, 6, 7]
    return lst[:3] + [x for x in lst[3:] if x % 3 != 0] + lst[6:]
```