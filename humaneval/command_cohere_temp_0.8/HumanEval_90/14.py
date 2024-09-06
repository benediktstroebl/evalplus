```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This Python script provides a function called `next_smallest` that solves the problem using sorting to find the 2nd smallest element. The function handles cases where the list has fewer than two elements without raising errors, returning None instead, as per the problem statement.