```python
def sort_even(lst):
    """This function sorts an input list l such that all odd indices become elements become equal to their original value, and the rest are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([9, 8, 7])
    [7, 8, 9]
    >>> sort_even([10, 10, 10])
    [10, 10, 10]
    """
    lst[:0] = [x if x % 2 != 0 else x // 2 for x in lst]
    return sorted(lst)
```