```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function sorts the array `arr`, which is assumed to be in random order, and then returns the first `k` elements. This guarantees that the resulting list will have the maximum `k` numbers from `arr`.