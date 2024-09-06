```python
def median(lst):
    # Sort the list
    lst.sort()
   
    # Get the median, which is the middle element of the sorted list
    middle = len(lst) // 2
    if len(lst) % 2 == 1:
        return lst[middle]
    else:
        return (lst[middle - 1] + lst[middle]) / 2
```