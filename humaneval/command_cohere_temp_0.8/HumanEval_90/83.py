```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element (excluding ties) with an efficient and concise one-liner. If the list has less than two elements, the function returns `None` to handle cases where determining the second smallest would be invalid.