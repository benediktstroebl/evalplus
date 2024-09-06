```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script provides a function called `next_smallest(lst)` that aims to return the second smallest element in a given list of integers `lst`. First, the list is sorted in ascending order using the `sort()` method. Then, the function checks whether the length of the list is less than 2. If the list is empty or contains only one element, indicating no distinct second smallest element, the function returns `None`. Otherwise, it returns the second element from the end of the sorted list, effectively capturing the second smallest element, as long as there are at least three distinct elements in the input list.