```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` sorts the input list of integers and retrieves the second element, returning it if it's a valid second-smallest element, and returning `None` if the list has less than two elements. This approach ensures the function is deterministic and follows the problem statement's given criteria.