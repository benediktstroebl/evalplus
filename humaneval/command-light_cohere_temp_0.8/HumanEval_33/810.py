```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sorted([1, 2, 3])
    [1, 2, 3]
    >>> sorted([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return sorted(l, key=lambda x: not_divisible(x, 3))

def not_divisible(x: int, m):
    """This function takes an integer x and an integer m, and returns 
    True if x is divisible by m, False otherwise."""
    return x % m == 0
```