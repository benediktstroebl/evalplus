```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` uses the Python built-in sorted() function to sort the given list. Then, it checks if the length of the list is less than 2. If so, it returns None, indicating that the list does not have a second smallest element. Otherwise, it returns the second element of the sorted list, which is the second smallest element of the original list.