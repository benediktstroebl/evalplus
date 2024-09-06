```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element (assuming indexing starts at 1) from the sorted list. If the list has less than two elements, it returns `None` to account for the lack of a second smallest value. This approach ensures a consistent and efficient solution.