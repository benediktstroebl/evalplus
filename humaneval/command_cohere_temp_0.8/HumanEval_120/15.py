```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This function takes an array `arr` and an integer `k` as input, sorts the array, and returns the maximum `k` elements in the array. This algorithm is simple and efficient, as its time complexity is O(k log n), where n is the length of the input array.