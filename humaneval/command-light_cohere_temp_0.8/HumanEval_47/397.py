```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test the function with different data
assert(median([-10, 4, 6, 1000, 10, 20]) == 15.0)
assert(median([1, 2, 3]) == 3)
assert(median([-20, -15, -10, -5]) == -5)
assert(median([10, 20, 30, 40, 30]) == 30)
```