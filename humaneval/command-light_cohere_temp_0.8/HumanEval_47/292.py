```python
def median(l):
    # Sort the list in ascending order
    l.sort()
    median = float('-inf')  # Initialize with negative infinity
    for i in range(len(l) // 2):
        median = l[i] + l[i + 1] / 2
    return median
# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([10, 20, 30, 15, 25]) == 20.0
assert median([]) == float('-inf')
```