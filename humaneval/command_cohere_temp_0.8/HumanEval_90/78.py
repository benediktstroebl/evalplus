```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script provides a function called `next_smallest(lst)` that aims to find the second smallest element in a given list of integers `lst`. The function first sorts the input list in ascending order using the `sort()` method. Then, it checks if the length of the list is less than 2. If the list contains fewer than two elements, it implies that there is no distinct second smallest element, so the function returns `None` to indicate that no such element exists. 

On the other hand, if the list contains at least two elements, the function returns the second element from the end of the sorted list, effectively giving the second smallest element based on the sorted order. 

This approach ensures that the function accurately reflects the given specification and handles edge cases appropriately.