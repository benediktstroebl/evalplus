```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` sorts the input list of integers and then retrieves the second element, returning it as the second smallest element in the list. The method returns `None` when the list has less than two elements. This handling ensures that the function adheres to the problem's requirements, returning the second smallest element when possible and notifying the absence of such an element when it is not.  It makes the function adaptable to various list configurations.