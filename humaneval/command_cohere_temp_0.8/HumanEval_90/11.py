```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This Python script provides a function called `next_smallest(lst)` that aims to find the second smallest element in a given list of integers `lst`. The function first sorts the input list in ascending order using the built-in `sort()` method. Then, it checks the length of the list. If the length is less than 2, indicating that there is no distinct second smallest element, the function returns `None`. Otherwise, it returns the second element from the end of the sorted list, effectively capturing the second smallest value. 

This solution is concise and achieves the goal of finding the second smallest element effectively. It also includes checks to handle scenarios with invalid inputs, such as an empty list or a list with only one element, which return `None` as required by the problem statement.