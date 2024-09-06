```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```

The function `next_smallest()` uses the Python built-in sorted() function to sort the input list regardless of list size. Then, if the length of the list is less than 2 (`len(lst) < 2`), indicating an insufficient number of elements to find the 2nd smallest, the function returns `None`. If the list length is 2 or more, the function returns the second element of the sorted list, which is the second smallest element of the original list.