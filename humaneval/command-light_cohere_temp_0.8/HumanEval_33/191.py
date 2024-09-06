```python
def sort_third(lst):
    """Sorts the list lts such that values divisible by three are moved to the front, while values not divisible by three are unchanged. The list is returned"""
    """
    lst[:] = [x for x in lst if x % 3 == 0]
    lst.remove(int(lst[0]) if lst[0] % 3 == 0)
    lst = [x if x not in lst else lst.insert(0, x) for x in lst]
    lst.sort_integers()
     # Sort the list
    return lst
```

This function takes a list `lst` as input and returns a sorted list, such that values divisible by three are moved to the front, while values not divisible by three are unchanged. The list is then removed of the first value that is divisible by three and then the list is sorted using the `sort_integers` function.