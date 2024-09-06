```python
def sort_third(lst):
    """Sorts the list l such that values not divisible by three are in their original order, while values divisible by three are sorted to the value of the corresponding original value.
    Args:
        lst: list
    Returns: list, list' contents are modified in place.
    """
    code:
    list_ = lst.copy()  #
    important to note here, the list lst is copied to avoid modifying the original list.
    lst[:] = [x for x in lst if x % 3 != 0]
    lst = [x for x in lst if x % 3 == 0]
    lst.append(x original lst)
    lst.copy() = list()
    list = lst
    return list
```