```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
The code defines a Python function `next_smallest()` that takes a list of integers as input. It sorts the list in ascending order and checks if the length of the list is less than 2. If the list has less than two elements, it returns `None`, indicating that there is no second-smallest element. However, if the list has two or more elements, it returns the second element of the sorted list, which is the second-smallest element in the original list.