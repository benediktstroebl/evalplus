```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```
The function 'next_smallest' sorts the input list and retrieves the second element, returning None if the list has less than two elements. This approach ensures a straightforward and efficient solution.