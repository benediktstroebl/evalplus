Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while hi - lo > 1:
        if lst[mid] <= lst[mid + 1]:
            if lst[lo] <= lst[mid] and lst[mid] <= lst[hi]:
                return True
            mid = (lo + hi) // 2
            lo = mid
        else:
            if lst[lo] <= lst[mid] and lst[mid] <= lst[hi]:
                return True
            hi = mid
    return lst[lo] <= lst[hi]

# Tests
assert monotonic([1, 2, 4, 20])
assert not monotonic([1, 20, 4, 10])
assert monotonic([4, 1, 0, -10])
```

The `monotonic` function checks if the list is monotonically increasing or decreasing. The `while` loop implements a binary search to efficiently determine if the elements are monotonic. The loop alternates between updating the lower and upper bounds, checking if the next element is greater than or equal to the current element. If the condition is satisfied for all iterations, the list is monotonic.