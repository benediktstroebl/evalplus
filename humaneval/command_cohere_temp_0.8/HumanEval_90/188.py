```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element of the sorted list. It returns `None` if the list has less than two elements. This algorithm is concise and efficient for this problem. 

This solution is optimized and cleaner than the one I initially provided, and it avoids the issue of assuming the list to be sorted while handling edge cases.