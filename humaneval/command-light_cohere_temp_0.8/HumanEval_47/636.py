```python
def median(lst):
    n = len(lst) // 2 + 1
    mid1 = lst[(n-1) // 2]
    mid2 = lst[n // 2]
    if lst[0] > mid1:
        return (mid1 + mid2) / 2
    else:
        return mid2
```
This code defines a function median that calculates the median of a list. The median is the value that divides the list into two groups with the same number of elements (even number of elements) and is the average of the two middle numbers.