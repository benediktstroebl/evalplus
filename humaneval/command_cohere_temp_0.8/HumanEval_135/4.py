```python
def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for idx, val in enumerate(arr):
        if idx == 0:
            continue
        if val <= arr[idx - 1]:
            max_idx = idx
            break
    return max_idx
```

The function `can_arrange` iterates over the non-empty array and compares each element with the preceding one. If any element is smaller than the previous one, its index is returned, otherwise, the loop continues until a suitable index is found. The loop terminates as soon MUST terminate because it is iterating over a finite set (the array), and it has a stopping condition (the first inconsistent index). 

This approach has a time complexity of O(n) where n is the number of elements in the array.