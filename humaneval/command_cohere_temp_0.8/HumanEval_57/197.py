Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while hi - lo > 1:
        if l[mid] <= l[mid - 1] and l[mid] <= l[mid + 1]:
            return True
        elif l[mid] >= l[mid - 1] and l[mid] >= l[mid + 1]:
            return True
        elif l[mid] > l[mid - 1] and l[mid + 1] > l[mid]:
            return True
        elif l[mid] < l[mid - 1] and l[mid + 1] < l[mid]:
            return True
        elif l[mid] >= l[mid - 1]:
            lo = mid
        elif l[mid] <= l[mid - 1]:
            hi = mid
        else:
            return False
        mid = (hi + lo) // 2
    return l[mid] <= l[mid - 1] or l[mid] >= l[mid + 1]

# Tests
assert monotonic([1, 2, 4, 20])
assert not monotonic([1, 20, 4, 10])
assert monotonic([4, 1, 0, -10])
assert monotonic([10, 10, 10, 10, 30])
assert not monotonic([10, 9, 8, 7, 6])
```

This script includes the `monotonic` function and some test cases to validate its behavior against the problem statement. You can add more test cases as needed. Simply copy and paste this code into a Python script to use it.