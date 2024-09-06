```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 3, 9, 2, 1, 20])
    [9, 2, 10, 1, 20]
    """
    lst = list(l)
    return sorted(set(range(len(l))), key=lambda ind: lst[ind] if ind != 3 else lst[ind-3]) + [lst[3]]
```