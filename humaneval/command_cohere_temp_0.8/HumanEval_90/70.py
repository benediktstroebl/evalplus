```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script sorts the input list and then retrieves the second smallest element, returning `None` if the list has less than two elements. This ensures the function handles various input scenarios correctly.