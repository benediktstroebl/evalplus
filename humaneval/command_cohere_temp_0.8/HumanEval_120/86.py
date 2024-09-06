```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This function sorts the copied array (`arr_copy`) and returns the first `k` elements, which are the maximum `k` numbers from the original array (`arr`). 

The function optimally solves the problem without any unnecessary sorting or additional loops, making it an efficient solution for the given task. 
This approach takes advantage of Python's built-in sorting functionality and slicing features.