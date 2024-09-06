```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```
The function `next_smallest()` uses the Python built-in sorted() function to sort the input list regardless of list size. Then, if the length of the list is less than 2, it returns None; otherwise, it returns the second element of the sorted list.