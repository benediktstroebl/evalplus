```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, `arr` and `k`. The function sorts the array and then returns the first `k` elements. Since the given `arr` is assumed to be a list of integers, the built-in Python sort function works correctly. The function is concise and efficient with a time complexity of O(log(n)) where n is the length of the input list. Additionally, the function runs independently without any external dependencies.