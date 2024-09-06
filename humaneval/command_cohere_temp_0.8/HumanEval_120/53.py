Here's a Python script that includes a function `maximum_k(arr, k)` to solve the problem:
```python
def maximum_k(arr, k):
    return sorted(arr)[-k:][::-1]
```
This function takes in an array `arr` and an integer `k` as inputs, and returns a sorted list of the maximum `k` numbers in the array. The output is achieved by using sorting to find the `k` maximum elements and then retrieving them from the sorted array using indexing. The `[::-1]` slicing operation reverses the sorted order to obtain the correct arrangement.