```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```
The function `next_smallest()` uses the built-in Python function `sorted()` to sort the given list. Then, it checks if the length of the list is less than 2. If it is, returning `None` handles the case where the list has only one or zero elements. Otherwise, it returns the second element of the sorted list, which is the second smallest element of the original list.