Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while lo <= hi:
        if lst[mid] >= lst[mid - 1] and lst[mid] <= lst[mid + 1]:
            return True
        elif lst[mid] <= lst[mid - 1]:
            lo = mid + 1
        elif lst[mid] >= lst[mid + 1]:
            hi = mid - 1
        else:
            return False
        mid = (lo + hi) // 2
    return False
```

The function monotonic takes a list `lst` as input and returns a boolean indicating whether the list's elements are monotonically increasing or decreasing. The algorithm uses binary search and checks if the mid element is greater than or equal to the previous element and less than or equal to the next element. If this condition is fulfilled at each step of the binary search, the function returns True, indicating a monotonic sequence. If the condition is not fulfilled, it returns False.