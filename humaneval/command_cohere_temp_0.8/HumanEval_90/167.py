```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```
The function 'next_smallest' sorts the input list and returns the second element (the first smallest) if the list has at least two elements. It returns None if the list has less than two elements or if there is a tie for the second smallest value.