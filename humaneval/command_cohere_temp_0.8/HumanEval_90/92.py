```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and returns the second element if the list has at least two elements. It returns `None` otherwise, which matches the specification for the given cases.