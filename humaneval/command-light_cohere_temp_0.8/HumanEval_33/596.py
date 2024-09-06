```python
def sort_third(lst):
    """Returns a list l' such that values at indices not divisible by three are in l' and values at indices divisible by three are in l' and are sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 11, 12, 13, 1, 4, 5, 6, 7])
    [1, 4, 5, 6, 7, 10, 11, 12, 13]
    >>> sort_third([21, 34, 12, 45, 56, 78, 89])
    Traceback (most recent call last):
      ...
    AssertionError: len([21, 34, 12, 45, 56, 78, 89]) != 4
```