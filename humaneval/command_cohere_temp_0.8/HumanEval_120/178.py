```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, `arr` and `k`, where `arr` is a list of integers and `k` is a positive integer. The function sorts the given array and returns the maximum `k` numbers as a list. This solution follows the spec outlined in the original problem prompt.

This function's time complexity is `O(log(n) * k)`, where `n` represents the length of the input array, as sorting an array takes linear time, and selecting the first `k` elements from the sorted array takes `k` times faster.

Note that this function assumes that the input is valid, i.e., the length of the array is in the range of \[1, 1000\), and the elements in the array are in the range of \[-1000, 1000\). If you need to handle invalid input, you may need to add further validation and adjustment before running the sorting and slicing operation.