```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 16, 3, 14, 13, 4])
    [3, 14, 4, 15, 2, 13, 10, 15, 16]
    >>> sort_third([21, 18, 9, 10, 20, 11, 8])
    [9, 10, 11, 18, 21]
    >>> sort_third([A, B, C, D, E, F, G, H, I])
    raise ValueError("Invalid input. Not a list of numbers")
```