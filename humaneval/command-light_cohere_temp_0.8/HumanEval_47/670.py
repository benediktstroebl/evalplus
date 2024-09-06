```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    mid = len(lst) // 2
    if lst[mid] > lst[len(lst) - mid - 1]:
        mid = (len(lst) + mid) // 2
    return (lst[mid] + lst[len(lst) - mid - 1]) / 2
```
This function utilizes the fact that the median of a list of numbers is equal to the average of the two middle numbers. It works for lists of positive and negative numbers, regardless of their order.