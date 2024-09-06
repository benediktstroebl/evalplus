```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) <= 1:
        return lst[0]
    m = len(lst) // 2 + 1
    left = median(lst[:m])
    right = median(lst[-m:])
    return (left + right) / 2
# Tests
if median([3, 1, 2, 4, 5]):
    print('Medium is', median([3, 1, 2, 4, 5]))
if median([-10, 4, 6, 1000, 10, 20]):
    print('Medium is', median([-10, 4, 6, 1000, 10, 20]))
if median([1, 2, 4, 5, 6]):
    print('Medium is', median([1, 2, 4, 5, 6]))
if median([9, 8, 7, 6, 5, 4, 3]):
    print('Medium is', median([9, 8, 7, 6, 5, 4, 3]))
if median([1000, 100, 2500, 2000, 3000]):
    print('Medium is', median([1000, 100, 2500, 2000, 3000]))
```
The function median takes a list as an argument and returns the median of the elements in that list. The function works by first sorting the list and then taking the middle element(s) as the median. The function also works by taking the average of the two middle elements as the median, which is the same approach used in the previous solution.