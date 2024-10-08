```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 6, 9, 1, 8])
    [1, 2, 6, 9, 8, 10]
    >>> sort_third([3, 2, 6, 8, 5, 4])
    [2, 6, 8, 5, 4, 3]
    >>> sort_third([11, 2, 5, 4, 6, 7])
    Traceback (most recent call last):
    ...
    ValueError: Only one element in list with length 4 found at index 1
```