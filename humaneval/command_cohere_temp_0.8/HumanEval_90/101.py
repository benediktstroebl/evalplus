```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The function `next_smallest()` sorts the input list and retrieves the second element, returning `None` if the list has less than two elements. This method ensures simplicity and efficiency in determining the second smallest number in a list. It is a robust solution for this problem. The Python built-in `sorted()` function sorts the list in place, and the resultant list is accessed via `lst[1]` to retrieve the second smallest element.