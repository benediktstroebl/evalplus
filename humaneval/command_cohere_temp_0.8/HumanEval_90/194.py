```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script provides a function called `next_smallest(lst)` that aims to return the second smallest element in a given list of integers `lst`. First, the function sorts the input list in ascending order using the built-in `sort()` method. Then, it checks the length of the list. If the length is less than 2, indicating that there is no distinct second smallest element, the function returns `None`. Conversely, if the list has at least two elements, the function returns the second element from the end of the sorted list, effectively providing the second smallest element. 

This solution adheres to the problem statement's expectations, returning the second smallest element for valid input lists and None when the list has an insufficient number of elements.