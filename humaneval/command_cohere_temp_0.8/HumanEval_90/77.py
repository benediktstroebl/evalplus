```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This Python script defines a function called `next_smallest` taking in one parameter, `lst`, which is the given list of integers. The function first sorts the list, then checks if the length of the list is less than 2; if so, it returns None, indicating that the list has either one or zero elements, both cases lacking a second smallest element. If the list has at least two elements, the function returns the second element of the sorted list, which is the second smallest element of the original list. This behavior matches the pattern expected by the problem's statement.