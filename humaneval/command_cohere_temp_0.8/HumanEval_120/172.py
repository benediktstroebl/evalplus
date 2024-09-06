Here's a Python script that contains a function named `maximum_k` that solves the problem:
```python
def maximum(arr, k):
    arr.sort()
    return arr[:k]
```
The function `maximum_k` takes in an array `arr` and an integer `k` as input, sorts the array, and returns the maximum `k` numbers from the sorted array. 

This solution does not require any additional import statements or modules as the method uses only the built-in Python `.sort()` and `[:k]` slice techniques.  It is also concise and less prone to errors due to the simplicity of the code.  Feel free to test it out with some cases and verify if it behaves as expected!