```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This function employs the Python built-in `sorted` function to sort the input list. Subsequently, it verifies if the length of the list is less than 2 and returns `None` if so. If the list contains at least two elements, the function provides the second smallest element, which is equal to the second element in the sorted list.