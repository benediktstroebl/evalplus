```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]

    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]

    >>> sort_third([10, 2, 3, 20, 40, 13, 4])
    [40, 13, 10, 2, 3, 20, 4]

    >>> sort_third([1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5, 6, 7]

    >>> sort_third([0.9, 9, 8, 0])
    [0, 8, 9]

    >>> sort_third([6, 5, 3, 4, 2, 1])
    [2, 3, 4, 5, 6]
    ```