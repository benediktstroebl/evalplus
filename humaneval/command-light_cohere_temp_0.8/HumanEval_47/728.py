```python
def median(lst):
    """Return median of elements in the list lst"""
    n = len(lst)
    if n % 2 == 0:
        m = (len(lst) // 2)
        return (lst[m - 1] + lst[m]) / 2
    else:
        return lst[n // 2]
#Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3]) == 3
assert median([-1, 3, 4]) == 1
```