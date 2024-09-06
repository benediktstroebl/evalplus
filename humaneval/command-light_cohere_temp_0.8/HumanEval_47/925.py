```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test 1:
assert median([3, 1, 2, 4, 5]) == 3.2

# Test 2:
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test 3:
assert median([1, 2, 3, 4, 5]) == 3.0

# Test 4:
assert median([10, 20, 30, 40, 30, 60]) == (30 + 40) / 2
```