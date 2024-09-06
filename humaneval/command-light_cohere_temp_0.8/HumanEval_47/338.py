```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test case 1
assert median([3, 1, 2, 4, 5]) == 3.67

# Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 3
assert median([5, 5, 6, 7]) == 5.0

# Test case 4
assert median([9, -9, -8, -7]) == 0
```