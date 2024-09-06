```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This Python script defines a function called `maximum` which takes two arguments - a list of integers `arr` and an integer `k`. This function sorts the array and returns a slice of the sorted array containing the maximum `k` elements.

The provided solution is efficient and uses Python's native sorting functionality, which is efficient for large arrays as it uses quadratic time complexity (O(n^2)) for sorting the array. The `copy()` method is used to ensure that the original list is not modified.