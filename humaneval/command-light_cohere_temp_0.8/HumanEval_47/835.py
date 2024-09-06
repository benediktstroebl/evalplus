```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    else:
        middle = len(lst) // 2
        left = median(lst[:middle])
        right = median(lst[middle:])
        return (left + right) / 2
``` 
This function performs a stable sorting of the list and takes the middle element of the sorted list as the median value.