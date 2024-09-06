```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
The function `next_smallest()` sorts the input list and returns the second smallest element if there are at least two elements. If the list has less than two elements, the function returns `None`. This approach ensures a consistent and efficient solution.