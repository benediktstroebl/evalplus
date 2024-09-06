```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This function sorts the copied array (`arr_copy`) and returns the first `k` elements, which are the largest `k` elements from the original array (`arr`). 

The function maximizes the use of the original array without modifications and returns the required output by slicing the sorted array. 

This approach adheres to the problem's requirement of not modifying the original array and instead provides a efficient and clean solution.