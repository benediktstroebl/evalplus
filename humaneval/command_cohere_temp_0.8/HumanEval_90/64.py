```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
The function `next_smallest()` sorts the input list of integers and retrieves the second-smallest element, handling cases where the list might have fewer than two elements by returning `None` to conform to the problem statement. 

Here's a concise version of the above, meant to emphasize the essential steps and logic:
```python
def next_smallest(lst):
    return sorted(lst)[1] if len(lst) > 1 else None
```

This version uses the built-in `sorted()` function with indexing to achieve the same result. It directly converts the unsorted list into a sorted list, and if there's more than one element, it captures the second-smallest one.