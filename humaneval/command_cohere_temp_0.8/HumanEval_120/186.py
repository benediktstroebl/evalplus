```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, namely `arr` and `k`. `arr` is the array containing integers, and `k` is the positive integer specifying the length of the returned list. The function sorts the given array and returns the first `k` elements, achieving the maximum value retention in the reduced list. 

This solution adheres to the problem's presented constraints and serves as a straightforward Python implementation to solve the problem. Feel free to test it against various input scenarios to verify its behavior.