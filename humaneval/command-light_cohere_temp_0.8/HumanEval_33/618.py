```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l.sort_list(l) = sorted(l, key=lambda x: not_divisible(x,3))
    l.sort_list(l) == l
def not_divisible(x, y):
    """ This function checks whether x is divisible by y, and returns True if it is divisible and False otherwise."""
    return ((x // y) == 0)
```