```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the third elements, while its values at the third elements
    that are divisible by three are equal to the values of the corresponding third elements of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 7, 8, 11, 3, 4, 5, 6])
    [2, 7, 8, 11, 3, 4, 5, 6, 10]
    >>> sort_third([1, 2, 3, 6, 5])
    Traceback (most recent call last):
      ...
    ValueError: 'list' object does not support item assignment hint hint
```