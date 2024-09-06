```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element, returning `None` if the list has less than two elements.  This solution is efficient in terms of time complexity, as sorting a list takes O(n log n) time, and the other operations are constant time.