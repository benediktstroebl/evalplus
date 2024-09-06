```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach takes advantage of Python's built-in sorting functionality to identify the smallest and second-smallest elements in the list efficiently, avoiding the need for explicit loops and conditional logic.