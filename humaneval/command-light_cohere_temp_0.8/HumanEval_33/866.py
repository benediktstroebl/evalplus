```python
def sort_third(lst):
    """Sorts the list l such that elements divisible by three are in their correct positions,
    and the remaining elements are in their original positions.
    Returns a result: list l'
    """
    lst[:] = [x for x in lst if x % 3 != 0]
    lst = [x for x in lst if x % 3 == 0]
    lst.sort()
    _ning on the result: lst
    return lst
```