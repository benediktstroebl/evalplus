```python
def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for idx, val in enumerate(arr):
        if val > arr[idx - 1] and idx > max_idx:
            max_idx = idx
    return max_idx
```

The function `can_arrange` iterates over the array, comparing each element to the one preceding it (or `None` if it's the first element). If an element is greater than its previous one and this is the largest such discrepancy so far, the function updates the `max_idx` variable to the current index. Finally, the function returns `max_idx` if it's a valid index, or -1 if the condition isn't met.