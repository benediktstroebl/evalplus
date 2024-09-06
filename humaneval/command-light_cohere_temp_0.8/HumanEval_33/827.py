```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the items that are not divisible by three, while its values at the items that are divisible by three are equal to the values of the corresponding items of l, but sorted.

    Test suite:
    >>> sorted(range(0,10))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> sort_third([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
    >>> sort_third([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    l = sorted(l, key=lambda x: not_divisible(x))
    l = l[:] + [x for x in l if _divisible(x)]
    return l

def _divisible(x):
    """This function takes an integer x and returns True if x is divisible by three, False otherwise."""
    return x % 3 == 0
```