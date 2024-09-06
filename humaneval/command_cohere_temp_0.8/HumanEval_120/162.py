```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]
```

This function `maximum` takes in an array `arr` and an integer `k` as inputs, sorts the array, and then returns the first `k` elements of the sorted array, which effectively are the maximum `k` numbers in the original array. 

This approach uses Python's native sort functionality to accomplish the task with a time complexity of O(log k * n) where n is the size of the input array. 

Please let me know if you would like me to explain how the algorithm works in depth or provide any further optimizations techniques!