```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```

This Python script provides a function called `next_smallest` that solves the problem as stated in the provided markdown code block. It first sorts the list of integers, and then returns the second element (second smallest number) in the sorted list. If the list has less than two elements, the function returns `None`, as there is no distinct second smallest element in such a list. This handling ensures the function's behavior matches the given requirements for the scenario when there isn't a clear second smallest number.