```python
def strange_sort_list(lst):
    """
    Do a strange sort of the list, then return it.
    
    Strange sorting is when you start with the minimum value,
    then take the maximum of the remaining integers, then the minimum, and so on.
    """
    if len(lst) == 0:
        return lst
    return [min(lst)] + [max(lst[:-1])] * (len(lst) - 2) + [min(lst[:-1])]

# Tests:
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
assert strange_sort_list([]) == []
```