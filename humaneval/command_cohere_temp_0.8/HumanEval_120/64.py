```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]
```

This function sorts the array and then returns the first k elements. Since the array is sorted in ascending order, these first elements will be the maximum elements. As the input states, the array `arr` is guaranteed to be sorted in linear time. Then, the slice `arr[:k]` can be retrieved in constant time.

The code provides a efficient solution to the problem in a straightforward manner, adhering to the specified requirements.