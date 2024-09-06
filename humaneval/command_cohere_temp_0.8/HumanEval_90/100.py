```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach takes advantage of Python's built-in sorting capability, which allows the list to be sorted in place. Since the list is sorted, the second-smallest element will be at the second position. However, if the list has less than two elements, it will return None to account for the lack of a second smallest number.