```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` sorts the input list of integers and then retrieves the second element, returning it as the second-smallest element or None if the list has less than two elements.