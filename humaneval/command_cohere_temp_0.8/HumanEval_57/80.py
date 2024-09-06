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
    return l[mid] <= l[mid + 1] or l[mid] >= l[mid - 1]
```

The function monotonic takes a list l as input and returns True if the elements in the list are monotonically increasing or decreasing. The function first checks if the length of the list is less than or equal to 1, returning True in such cases as the list is considered to be automatically monotonic. Then, it uses binary search to determine whether the list is monotonic in the middle, and returns True if the middle elements are in order and either endpoint is not in contradiction with the middle element.  Overall, the script evaluates the list and determines if the elements are in a monotonic pattern, returning True for valid inputs and False otherwise.  This integrates the requirements of the problem with the provided tests.