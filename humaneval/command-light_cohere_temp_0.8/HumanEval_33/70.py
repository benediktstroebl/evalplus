```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.

    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    # sort elements which are not divisible by 3
    s = []
    for i in range(len(l)):
        if l[i] % 3 != 0:
            s.append(l[i])

    # append the same elements which are divisible by 3
    l = l + s

    # sort elements which are divisible by 3
    s = []
    for i in range(len(l)):
        if l[i] % 3 == 0:
            s.append(l[i])

    l = l + s

    return l
```