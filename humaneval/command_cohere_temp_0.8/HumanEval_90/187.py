```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element (index 1) of the sorted list. If the list has less than two elements, it returns `None` to account for the edge case where there is no distinct second smallest element. This ensures the function works as expected for the scenarios outlined in the problem description.