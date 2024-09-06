```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 11, 99])
    [99, 11, 22, 33]
    """
    l_sort = []
    for x in l:
        if x % 3 == 0:
            l_sort.append(x_int(x))
        else:
            l_sort.append(x_int(x))
    l_sort.append(l[-1])  # Add last element to the end of l_sort
    l = l_sort
    return l
```