```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function sorts the input array and then returns the first k elements. Since these are the first k elements, they are also the maximum k numbers in the original array. 

This code solves the given problem in a straightforward manner, which results in a time complexity of O(log k) for the kth largest elements.