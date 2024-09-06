```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This Python script defines a function `next_smallest` that, when given a list of integers, will return the second smallest element in that list, or `None` if the list has less than two elements. This function uses sorting to rank the elements of the list, and then retrieves the second element (which should be the second smallest if the list is sorted).