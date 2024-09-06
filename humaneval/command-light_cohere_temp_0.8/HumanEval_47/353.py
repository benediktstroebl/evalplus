```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test 1:
assert median([3, 1, 2, 4, 5]) == 3.4

# Test 2:
assert median([-10, 4, 6, 1000, 10, 20]) == 15
```