```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, namely `arr` and `k`. `arr` is the array containing integers, and `k` is the positive integer specifying the length of the returned list. The function works by sorting the array `arr` and then returning the first `k` elements from the sorted array, which are the maximum `k` numbers in the original array. 

This approach efficiently solves the problem in O(log(n) + k) time complexity, where n is the length of the input array. It will be efficient irrespective of the order of the elements in the original array. If the original array is already sorted, it can be processed in O(k) time. 

This solution assumes that the positive integer `k` is less than or equal to the length of the input array. If `k` is greater than the array's length, a partial list of the maximum numbers will be returned.