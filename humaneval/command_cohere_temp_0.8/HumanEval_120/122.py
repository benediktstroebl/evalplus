```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```
This function sorts the input array and then returns the first k elements. It can be easily tested by calling the function with a test case like: ```python
assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
``` 
The code is succinct and achieves a time complexity of O(k log n) due to the initial sort, followed by a constant-time slice operation. If the input is already sorted, it can be further optimized to run in O(k) time using a segmented subset maximum selection algorithm.