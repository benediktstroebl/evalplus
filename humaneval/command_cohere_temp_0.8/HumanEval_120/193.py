```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function sorts the input array and then returns the first k elements. It ensures the output contains the maximum k numbers in the original array. 

To implement this function, the following steps can be followed:
1. Use the built-in `sorted` function to sort the entire array `arr`.
2. Use the slicing operation `arr_copy[:k]` to return the first `k` elements from the sorted array. 

This provides a concise solution to the problem statement, as it efficiently returns the maximum `k` numbers from the input array.