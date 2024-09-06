```python
def median(lst):
    """Return median of elements in the list lst"""
    n = len(lst)
    if n % 2 == 1:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
#Test cases
# Order of elements in the list has no effect on the result
median([-10, 4, 6, 1000, 10, 20]) == 15.0
median([4, 6, 10, -10, -20]) == -10.0
median([3, 1, 2, 4, 5]) == 2.0
median([20, 10, 6, 4, -10]) == 4.0
median([1000, 2000, 1000, -10]) == 1000
```