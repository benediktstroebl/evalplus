```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This Python script provides a function called `next_smallest()` that solves the problem using a straightforward algorithm. It sorts the input list and returns the second element (assuming the list has at least two elements). If the list has fewer than two elements, it returns None to reflect that there is no second-smallest value. This approach ensures the function is deterministic and consistently returns the correct result for the given test cases.