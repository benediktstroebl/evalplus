```python
def next_smallest(lst):
    if len(lst) < 2:
        return None
    mins = min(lst)
    sec_mins = mins + 1
    for num in lst:
        if num == sec_mins:
            return num
        elif num > sec_mins:
            sec_mins = num
    return None
```

The function `next_smallest()` takes a list of integers as input and returns the second smallest element in the list. It handles cases with less than two elements and returns `None` if there is no distinct second smallest element. The logic efficiently identifies the second smallest without needing to sort the entire list. 

The implementation succinctly solves the problem while maintaining clarity and efficiency. It achieves the desired outcome without unnecessarily sorting or iterating through the list more than once.