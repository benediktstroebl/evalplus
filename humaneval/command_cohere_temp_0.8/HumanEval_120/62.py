```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, `arr` and `k`, where `arr` is a list of integers and `k` is a positive integer. The function sorts the given list and returns the maximum `k` numbers as specified.

This solution is efficient and uses a time complexity of O(nlogn), where n is the length of the input list `arr`.