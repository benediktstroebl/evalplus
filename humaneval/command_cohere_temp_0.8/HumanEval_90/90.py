```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` uses the Python built-in sorted() function to sort the list regardless of list size. If the length of the list is less than 2, the function returns None to comply with the problem statement. If not, the function returns the second element of the sorted list, which is the smallest element after the smallest element of the original list.