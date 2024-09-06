```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 14, 11, 6])
    [10, 11, 6, 15, 14, 2]
    >>> sort_third([0.001, 0.0, 0])
    list([0.001, 0.0, 0])
    list([0.1, 0.0, 0])
    list([0.001, 0.0, 0])

    """

```