```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
The function `next_smallest()` sorts the input list of integers and retrieves the second-smallest element, returning `None` if the list has less than two elements. This method ensures consistent and efficient retrieval of the second-smallest value.