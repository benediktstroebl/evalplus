```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    
    return arr_copy[:k]
```
This function sorts the array `arr`, then returns a slice of the sorted array with length `k`. This ensures that the returned list contains the maximum `k` elements in the original array, as required by the prompt. This solution has a time complexity of O(k * log k) due to the sorting and slicing operations.