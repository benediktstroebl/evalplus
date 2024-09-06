Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```
The function `maximum_k` takes in an array `arr` and an integer `k` as input, sorts the array, and then returns the first `k` elements from the sorted array, achieving a time complexity of `O(log k)` due to the sorting process. 

This approach is efficient even for large inputs because sorting takes advantage of temporal coherence.