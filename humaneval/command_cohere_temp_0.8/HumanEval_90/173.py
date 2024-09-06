```python
def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    lo, hi = 0, len(lst) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] == lst[mid + 1]:
            return lst[mid]
        elif lst[mid] > lst[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return None
```

The algorithm uses a *binary search* approach to efficiently find the second smallest element in the list, reducing the search space by half each time. It leverages the property that the second smallest element and the smallest element are not equal, ensuring a correct and efficient solution.