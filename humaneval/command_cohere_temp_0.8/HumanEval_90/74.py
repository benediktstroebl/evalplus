```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and returns the second element (the first small element) if the list has at least two elements. The function returns `None` if the list has less than two elements. This aligns with the problem's expectations.