```python
def can_arrange(arr):
    n = len(arr)
    if n == 0:
        return -1
    max_idx = -1
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            max_idx = i+1
            break
    return max_idx
```

The function `can_arrange` iterates over the array from index `0` to `n-2`, where `n` is the length of the array. It checks if each element is greater than or equal to the subsequent element. If a suitable element is found, its index is returned, and the loop is terminated using the `break` statement. If no such element is found, the function returns `-1`.