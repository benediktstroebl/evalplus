```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function sorts the array `arr`, then returns the first `k` elements from the sorted array, ensuring that they are the maximum elements given the constraint `k`. 

This solution has a time complexity of O(klog(n)) where k is the target number of elements and n is the input size. This is efficient as we only need to extract k elements from the sorted array, and sorting itself has a time complexity of O(nlog(n)). 

The space complexity is O(1) since the maximum function does not require any additional space.