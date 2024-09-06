```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element, returning `None` if the list has less than two elements. This method ensures consistent and efficient retrieval of the second smallest element, handling various input scenarios as specified in the problem.