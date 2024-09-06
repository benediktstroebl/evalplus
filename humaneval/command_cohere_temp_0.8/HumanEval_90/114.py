```python
def next_smallest(lst):
    lst = sorted(lst)
    if len(lst) < 2:
        return None
    else:
        return lst[1]
```
This approach takes the list and sorts it with `sorted()`. As a result, the smallest element will be at index 0, and the second smallest element will be at index 1. Just return the element at index 1, and we are done!

The None scenarios are handled naturally through the code's behavior of returning the second smallest element only if the list has more than one element. 

This is a concise and effective solution for the given problem. 

**NOTE:** This solution works if the list elements are integers. For floating-point numbers, the `sorted()` function will be ordered in ascending format.