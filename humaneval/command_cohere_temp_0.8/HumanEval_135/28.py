```python
def can_arrange(arr):
    n = len(arr)
    if n <= 1:
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

The function `can_arrange` iterates through the array, comparing each element to the previous one. If an element is smaller than or equal to the previous one, it is ignored. When an element greater than the previous one is found, it is recorded as the largest index that satisfies the condition and the loop terminates. The loop will only run for `n-1` iterations as it skips the last element (the second-to-last one in the loop) which is always compared to the last element which is checked immediately after the loop. As a result, this solution's time complexity is O(n) .