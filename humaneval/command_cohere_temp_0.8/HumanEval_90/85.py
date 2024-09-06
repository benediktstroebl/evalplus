```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```
The function `next_smallest()` sorts the input list and returns the second element of the sorted list. The list should have at least two elements; otherwise, it returns None.