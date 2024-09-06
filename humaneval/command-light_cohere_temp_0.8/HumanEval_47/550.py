```python
def median(lst):
    """Return the median of the list"""
    if len(lst) % 2 == 1:
        return (lst[int((len(lst)-1) / 2)] + lst[len(lst)-1]) / 2
    return lst[(len(lst) - 1) ]

# Test cases
median([-10, 4, 6, 1000, 10, 20]) # 15.0
median([1, 2, 3, 4]) # 3
median([-10, 4, 6, 7, 8, 9]) # 8
median([-5, -10, -8, -9, -3]) # -8
```