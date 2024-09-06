```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and returns the second element (second smallest) if the list has at least two elements. Otherwise, it returns `None`.