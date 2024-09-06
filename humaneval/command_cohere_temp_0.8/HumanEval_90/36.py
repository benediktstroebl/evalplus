```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```
The function 'next_smallest' sorts the input list and retrieves the second element (assuming the list has at least two elements), returning None if the list is empty or has just one element. This solution adheres to the problem's specifications, efficiently determining the next smallest element in a given list of integers.