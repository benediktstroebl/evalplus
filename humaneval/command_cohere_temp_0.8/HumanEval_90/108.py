```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This Python script defines the function `next_smallest()`, which takes a list of integers as input. It starts by sorting the input list in ascending order. Then, it checks if the length of the sorted list is less than 2. If so, it returns `None`, indicating that there is no second smallest element. However, if the length of the list is 2 or more, it returns the second element of the sorted list, effectively giving you the second smallest element of the original input list.