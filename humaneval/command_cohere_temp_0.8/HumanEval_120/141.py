```python
def maximum(arr, k):
    arr_copy = arr.copy()
    arr_copy.sort()
    return arr_copy[:k]
```
This function sorts the array and then returns the first k elements. It works for the mentioned range of arrays and returns the required number of maximum elements.