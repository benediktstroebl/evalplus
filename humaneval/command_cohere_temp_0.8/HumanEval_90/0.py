```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script provides a function called `next_smallest(lst)` that aims to return the second smallest element in a given list of integers `lst`. To accomplish this, the function sorts the input list in ascending order using the `sort()` method. Then, it checks if the length of the list is less than 2. If the list contains only one element or is empty, there is no distinct second smallest element, so the function returns `None` to indicate that there is no second smallest. 

However, if there are at least two elements in the list, the function returns the second element (index -1), which corresponds to the second smallest element in the original list. This approach is both simple and efficient, as it only requires a single pass through the list and can handle any type of list correctly.