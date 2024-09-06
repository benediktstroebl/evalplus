```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 6, 7, 18, 5])
    [10, 6, 15, 5, 7, 18, 2]
    >>> sort_third([10, 1, 2, 13, 18, 5, 3, 4, 7])
    [1, 2, 4, 7, 10, 13, 18, 5]
    """
    new_list = []
    for x in l:
        if x % 3 == 0:
            new_list.append(x(x))
    else:
            new_list.append(x(x))
    return new_list
```