```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```
This function sorts the input array and then returns the first k elements since they will be the maximum ones. The function is straightforward and doesn't require any additional libraries. It uses the built-in `sorted` function to sort the array and slicing to return the relevant chunk.