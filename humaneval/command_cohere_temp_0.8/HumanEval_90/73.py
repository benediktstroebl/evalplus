```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    return lst[1]
```

The function `next_smallest()` uses the Python built-in sorted() function to sort the input list regardless of list size. Then, it checks if the length of the list is less than 2. If the list is empty or has only one element, it returns None, as there is no 2nd smallest element. If the list has more than one element, it returns the second element of the sorted list, which is the second smallest element in the original list.