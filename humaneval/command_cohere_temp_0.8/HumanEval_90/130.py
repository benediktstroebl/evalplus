```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

The function `next_smallest()` sorts the input list of integers and retrieves the second element, returning it if the list has at least two elements. If the list has less than two elements, it returns `None` to reflect the absence of a distinct second-smallest number. This method avoids the need for additional logic and assumptions by taking advantage of the sorted list's structure, making it both effective and generically applicable.