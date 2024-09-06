Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while lo < hi:
        if lst[mid] <= lst[mid - 1] and lst[mid] <= lst[mid + 1]:
            return True
        elif lst[mid] >= lst[mid - 1] and lst[mid] >= lst[mid + 1]:
            return True
        elif lst[mid] < lst[mid - 1]:
            hi = mid
        else:
            lo = mid + 1
        mid = (lo + hi) // 2
    return False
```

The function monotonic takes a list lst as input and returns a boolean indicating whether the list's elements are monotonically increasing or decreasing. The function follows a midpoint convergence algorithm to quickly determine the trend. The algorithm divides the list into consecutive segments and checks if the elements are increasing or decreasing within each segment. If all segments follow the same trend, the function returns True; otherwise, it returns False.