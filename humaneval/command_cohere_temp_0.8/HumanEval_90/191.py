```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This function sorts the input list and returns the second element of the sorted list (the smallest element if the list has only two elements). If the list has less than two elements, the function returns None. The algorithm runs in O(log n) time, which is the runtime of the built-in sort method for Python lists.