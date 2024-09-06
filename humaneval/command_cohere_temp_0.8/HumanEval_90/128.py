```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
The function `next_smallest()` sorts the input list of integers and retrieves the second-smallest element, or `None` if the list has less than two elements. It works for both empty and non-empty lists, satisfying the given test cases.