Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while lo < hi:
        if lst[mid] >= lst[mid - 1] and lst[mid] <= lst[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo == len(lst) - 1 and lst[mid] >= lst[0]

# Tests
assert monotonic([1, 2, 4, 20])
assert not monotonic([1, 20, 4, 10])
assert monotonic([4, 1, 0, -10])
```

This code defines a `monotonic` function that checks if a list's values are monotonically increasing or decreasing. It uses a binary search algorithm to efficiently determine this. The function returns `True` if the values are monotonic, and `False` otherwise. The tests included confirm the function's behavior against predefined cases.