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

The function `can_arrange()` iterates over the non-empty array and for each element checks if it is greater than the previous one, and if so, keeps the index. The loop terminates when this condition no longer holds, returning the maximum index found. As the array contains no duplicates, the first iteration (idx = 1) is the fastest comparison and the loop will always terminate with the correct index or -1 if none is found. 

The approach guarantees a linear time complexity of O(n), with n being the number of elements in the array, making it an efficient solution.