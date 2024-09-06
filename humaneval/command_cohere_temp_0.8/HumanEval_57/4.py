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
    return False
```

The `monotonic` function checks if the list `l` has elements that are monotonically increasing or decreasing. The algorithm utilizes a binary search to efficiently determine the nature of the list. The binary search iteratively compares the middle element with the elements on its left and right sides. If the middle element is greater than the one on its left and smaller than the one on its right, the list is monotonically increasing; conversely, if the middle element is smaller than the one on its left and greater than the one on its right, the list is monotonically decreasing. Otherwise, the algorithm iterates further to find the point of transition. The algorithm's efficiency is evident when dealing with long lists, as it minimizes the number of comparisons needed.