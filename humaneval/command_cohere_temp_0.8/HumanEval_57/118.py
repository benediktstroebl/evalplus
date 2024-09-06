Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while lo <= hi:
        if lst[mid] <= lst[mid - 1] and lst[mid] <= lst[mid + 1]:
            return True
        elif lst[mid] >= lst[mid - 1] and lst[mid] >= lst[mid + 1]:
            return True
        elif lst[mid] > lst[mid - 1] and lst[mid + 1] > lst[mid]:
            lo = mid + 1
        elif lst[mid] < lst[mid - 1] and lst[mid] < lst[mid + 1]:
            hi = mid - 1
        mid = (lo + hi) // 2
    return False
```
The function monotonic takes a list, lst, as input and returns a boolean indicating whether the list is monotonic, i.e., if its elements are either increasing or decreasing. The algorithm utilizes a binary search and takes advantage of the list symmetry to efficiently determine the monotonicity. A list is considered monotonic if its elements are either increasing (as in [1, 2, 3, 4]) or decreasing (as in [4, 3, 2, 1]). The implementation carefully examines the middle element compared to the elements on either side and determines if the list is monotonic, providing a compact and efficient solution in a self-contained manner.