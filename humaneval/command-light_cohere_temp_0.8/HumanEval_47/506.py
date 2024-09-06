```python
def median(lst):
    """Return median of elements in the list lst."""
    lst.sort()
   
    # Sort the sorted list in ascending order.
    length = len(lst)
    middle = length // 2
    if length % 2 == 0:
        return (lst[middle-1] + lst[middle]) / 2
    else:
        return lst[middle]

# Test cases
median([3, 1, 2, 4, 5]) # 3
median([-10, 4, 6, 1000, 10, 20]) # 15.0
median([2, 4, 6, 8, 1, 3]) # 4
median([1, 2, 3, 4, 5, 6]) # 4
median([-5, -2, -8, -3, -1, -4]) # -8
```
This function will take a list of numbers and return the median value of those numbers. The function first sorts the add the list in ascending order and then finds the median value.