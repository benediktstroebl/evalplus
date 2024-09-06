```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` sorts the input list of integers and then retrieves the second element from the sorted list. If the list has less than two elements, it returns `None` to account for the lack of a second smallest value. This approach ensures a straightforward and efficient solution to the problem.