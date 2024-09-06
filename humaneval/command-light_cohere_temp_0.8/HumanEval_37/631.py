```python
def sort_even(lst):
    """Sorts the list lst such that values of even indices are equal to each other and all values are sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    new_list = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            new_list.append(lst[i])
    new_list.append(lst[i+2])
    return new_list
```