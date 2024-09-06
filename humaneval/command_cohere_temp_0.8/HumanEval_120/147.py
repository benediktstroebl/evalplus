```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```
This function sorts the input array and then returns the first k elements. It can be easily adapted to other problems that involve sorting or maximum values.