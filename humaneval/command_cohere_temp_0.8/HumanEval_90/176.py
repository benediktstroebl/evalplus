```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This Python script defines a function called `next_smallest`, which takes a list of integers as input. It starts by sorting the input list in ascending order using the `sorted` function. Then, it checks whether the length of the sorted list is less than 2. If the list has less than two elements, it means there is no distinct 2nd smallest element, so the function returns `None`. Otherwise, if the list has two or more elements, the function returns the second element of the sorted list, effectively giving you the 2nd smallest element of the original input list.