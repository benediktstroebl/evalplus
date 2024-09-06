```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```

The function `next_smallest()` uses the Python built-in sorted() function to sort the list regardless of list size. The function returns `None` if the length of the list is less than 2 to comply with the None return for lists of size 1 or less. And for lists of size 2 or more, it returns the second element after sorting.