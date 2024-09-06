```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]

    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]

    >>> sort_third([10, 2, 7, 8, 1, 3, 4])
    [1, 2, 7, 8, 3, 4, 10]
    """
    return sorted(l, key=lambda x: not_divisible(x, 3))

def not_divisible(x: int, y: int):
    return (x // y) == 0
```