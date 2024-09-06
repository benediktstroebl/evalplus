```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
test_median = []
for i in range(0, 10, 2):
    test_median.append([i, -10, i, i+1, i*2])

assert median([10, 10, 20]) == 10
assert median([10, 20, 30]) == 20
assert median([10, 10, 10]) == 10
assert median([5, 10, 15]) == 15
assert median([2, 8, 16, 18]) == 16
assert median([]) == 0
assert median([10, -10, 20]) == 10
assert median([10, 20, 30, 40]) == 30
```