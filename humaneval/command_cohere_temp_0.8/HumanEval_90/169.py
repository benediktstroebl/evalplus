```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` sorts the input list of integers and retrieves the second element, returning it if the list has at least two elements. If the list has less than two elements, it returns `None` to indicate that there is no second-smallest element. This approach ensures simplicity and efficiency in finding the second smallest element among a list of integers.