```python
def sort_even(lst):
    """Sorts a list l such that all odd indices are preserved, and the values at even indices match those of l, but are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    >>> sort_even([10, 2, 4, 8, 1])
    [1, 2, 4, 8, 10]
    """
    new_list = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            new_list.append(lst[i])
    else:
        new_list.append(lst[i] + 1)
    return new_list
```