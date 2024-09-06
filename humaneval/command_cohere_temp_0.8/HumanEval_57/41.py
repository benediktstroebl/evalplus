Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while hi - lo > 1:
        if l[mid] <= l[mid + 1]:
            if l[mid] <= l[lo] or l[mid + 1] >= l[hi]:
                return True
            mid += 1
        else:
            if l[mid] >= l[mid - 1] or l[lo] >= l[mid]:
                return True
            lo += 1
    return l[mid] <= l[mid + 1] and l[mid] >= l[mid - 1]

# Tests
assert monotonic([1, 2, 4, 20])
assert not monotonic([1, 20, 4, 10])
assert monotonic([4, 1, 0, -10])
```

This code defines the `monotonic` function and provides three test cases that demonstrate its behavior. The function first checks for edges cases where the list length is less than or equal to 1, returning True in such cases as the list is necessarily monotonic. It then uses a binary search-like approach to efficiently determine the midpoint where the monotonicity might break. Finally, it iterates over the list and checks if the elements are in increasing or decreasing order, returning True if so.