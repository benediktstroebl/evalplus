```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This Python script defines a function called `maximum` that takes two arguments - a list of integers `arr` and an integer `k`. This function sorts the list `arr` and then returns the first `k` elements of the sorted list, effectively providing a list of the maximum `k` numbers in the original input list. 

This approach efficiently solves the problem without any unnecessary complexity, making it suitable for handling lists of various sizes and data structures.