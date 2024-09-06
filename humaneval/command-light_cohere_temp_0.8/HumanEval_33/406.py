```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 99, 1, 99, 99, 22, 33, 11])
    [11, 22, 33, 99, 99, 99, 22, 33, 11, 99]
    """
    l[:]:sort(key=lambda x: not_is_divisible(x,3))
    l = [x for x in l if not_is_divisible(x,3)]
    return l

def not_is_divisible(x, y):
    """Returns True if x is divisible by y, False otherwise."""
    return (x//y) == 0
```