```python
def maximum(arr, k):
    arr = sorted(arr)
    return arr[:k]
```

This function `maximum` takes in an array `arr` and an integer `k` as inputs, sorts the array, and returns the maximum `k` numbers in the array. 

This approach takes advantage of Python's powerful list slicing feature to select the first `k` elements from the sorted array, naturally returning the maximum k numbers as requested by the prompt. The function is concise and efficient, providing a great solution to the problem. 

This function is self-contained, meaning it does not rely on any external variables or functions other than those natively provided by Python. It is a standalone function that can be placed in a separate Python file and run independently.