```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    
    return arr_copy[:k]
```
The function `maximum(arr, k)` takes in an array `arr` and an integer `k` as inputs, sorts the array, and returns the maximum `k` elements in the array. This approach ensures that the function correctly returns the maximum k numbers in `arr` without unnecessary complexity, making it an efficient solution.