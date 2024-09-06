```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script sorts the list of integers and then returns the second smallest element, or `None` if the list has less than two elements.