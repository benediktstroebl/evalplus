```python
def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    prev = arr[0]
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        max_idx = idx
        break
    return max_idx
```

The function works by initially assuming the maximum index of a non-decreasing element is the first index (idx=1). It then checks all the following elements, and if any element is greater than the previous one, it assigns the current index as the max_idx and breaks the loop. Ultimately, the function returns the max_idx value.