```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 11, 99, 99, 88, 22])
    [99, 11, 22, 33, 88, 99, 22, 11]
    """
    l = [1, 2, 3]
    for i in range(len(l)):
        if l[i] % 3 != 0:
            l[i], l[i] = l[i], l[i] + 1
    return l
```