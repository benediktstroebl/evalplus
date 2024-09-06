```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```

This function `next_smallest()` sorts the list of integers and returns the second element if the list has at least two elements. Otherwise, it returns `None`.