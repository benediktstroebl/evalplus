```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element (the first being the smallest) from the sorted list. If the list has less than two elements, it returns `None` to account for the edge cases specified in the problem description.