```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach employs the Python built-in sorting function, `sort()`. The list is sorted in ascending order, and the second last element returned as the 2nd smallest element, regardless of the original list's order. This ensures the function's behavior aligns with the given test cases.