```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This Python script provides a function called `next_smallest` that takes a list of integers as input. It sorts the list in ascending order and then retrieves the second element, representing the second smallest number. If the list has less than 2 elements, it returns `None` to accommodate cases with no distinct second smallest value. This function's behavior aligns with the problem's specification, returning the 2nd smallest element of the list while handling edge cases.