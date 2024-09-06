```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]

    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]

    >>> sort_third([10, 2, 6, 3, 9, 8, 1])
    [1, 2, 6, 3, 9, 8, 10]

    >>> sort_third([4, 2, 8, 1, 3, 5])
    [2, 1, 8, 3, 5]

    """
    l_copy = list(l)
    l_half = [i for i in l_copy if i % 3 == 0]
    l_odd = [i for i in l_copy if i % 3 != 0]
    l_even = [i for i in l_copy if i % 3 == 0]

    l_even = [i + j for i, j in zip(l_even, l_even)]

    l_half = [i + j for i, j in zip(l_half, l_half)]

    l_half = sorted(l_half)

    l_odd = sorted(l_odd)

    l_copy = l_even + l_half + l_odd

    return l_copy
```