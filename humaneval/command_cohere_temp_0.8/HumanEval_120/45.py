```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This function `maximum` takes in two parameters, `arr` and `k`. The idea is to copy the sorted array `arr_copy` and return a slice of it with length `k`. This will return the maximum k numbers in `arr`. 

### Here is the Markdown code block with the above Python script:
```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```