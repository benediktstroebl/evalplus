```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 7, 8, 1, 6])
    Traceback (most recent call last):
      File "<string>", line 4: ValueError: cannot convert list to int (input '6')
    """
    l[:] = [x for x in l if x % 3 == 0]
    return l
```