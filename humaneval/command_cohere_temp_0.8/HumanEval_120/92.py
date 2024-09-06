Here's a Python script that contains a function named `maximum_k` that addresses the problem described in the markdown code block:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```

This function sorts the input array and then returns a sliced version of the array, retaining the top `k` elements. This ensures that the returned list contains the maximum `k` numbers in the input array.