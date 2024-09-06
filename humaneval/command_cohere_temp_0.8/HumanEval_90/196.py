```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` sorts the input list of integers and retrieves the second element, returning it if it's present, or `None` if the list has less than two elements. This method works for lists containing negative integers as well and aligns with the problem statement in the provided code block. 

This solution is efficient and does not require any additional imports; it leverages Python's built-in `sorted()` function and the list's indexing capability.