```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test case: Median of [-10, 4, 6, 1000, 10, 20]
result = median([-10, 4, 6, 1000, 10, 20])
assert result == 15.0

# Test case: Median of the odd elements only: [-10, 4, 6]
result = median([-10, 4, 6, 1000, 10])
assert result == 6
```