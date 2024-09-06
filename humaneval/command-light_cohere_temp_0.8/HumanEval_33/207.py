```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the indices that are divisible by three are equal to the values of the corresponding index of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 8, 11])
    Traceback (most recent call last):
      File "<stdin>", line 6, in <module>
        raise ValueError("list index out of range")
    ValueError: list index out of range
    """
    lst[::3] = lst[::3] + lst[1::3]
    return lst
```