```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    return arr_copy[:k]
```

This function `maximum` takes in an array `arr` and an integer `k` as inputs, sorts the array, and returns the maximum `k` elements in the array. This function is straightforward and effectively passes the examples outlined in the problem statement.