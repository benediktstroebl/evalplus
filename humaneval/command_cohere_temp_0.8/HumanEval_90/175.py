```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This approach takes the list and sorts it using the `sorted` function. The function returns the second element (index 1) of the sorted list. However, if the list has less than 2 elements, the function returns `None` to comply with the problem's specifications. 

Here is a concise version of the above response for code readability:
```python
def next_smallest(lst):
    return sorted(lst)[1] if len(lst) > 1 else None
```

This approach takes the list and sorts it in ascending order using the `sorted` function. It then returns the second element of the sorted list. However, if the input list has less than two elements, the function returns `None` to account for the edge case specified in the problem.