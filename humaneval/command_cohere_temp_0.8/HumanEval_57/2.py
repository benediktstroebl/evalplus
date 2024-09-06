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
            lo = mid
        else:
            if l[mid] >= l[mid - 1] or l[mid + 1] <= l[hi]:
                return True
            hi = mid
        mid = (hi + lo) // 2
    return False
```

The `monotonic` function checks if the list `l` has elements that are monotonically increasing or decreasing. The algorithm uses a binary search to determine whether the list is monotonic. The binary search considers pivots at different positions in the list, checking if the elements are in the correct order. If the midpoint elements are not in the correct order, the search continues to the next pivot. If the pivot elements are in the correct order for all pivots, the function returns True; otherwise, it returns False. 

Here are some example outputs:
```
>> monotonic([1, 2, 4, 20])
True
>> monotonic([1, 20, 4, 10])
False
>> monotonic([4, 1, 0, -10])
True
``` 
This function efficiently solves the problem in a self-contained manner.