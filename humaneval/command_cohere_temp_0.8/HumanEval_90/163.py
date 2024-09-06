```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element (assuming the list has at least two elements). If the list has fewer than two elements, it returns None to handle cases where the second smallest element doesn't exist.