```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]
```

This function sorts the array and then returns the first k elements using the slice operator. Since the array is sorted in ascending order, these first k elements will be the maximum ones. Note that the function assumes that k specifies the number of elements to return and not the index to stop at. Adjust the function if this is not the intended interpretation.