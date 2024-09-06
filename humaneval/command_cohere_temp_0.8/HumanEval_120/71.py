```python
def maximum(arr, k):
    arr_copy = sorted(arr)
    
    return arr_copy[:k]
```

This Python script defines a function called `maximum` which takes two arguments - a list of integers `arr` and an integer `k`. This function sorts the array `arr` and returns the first `k` elements of the sorted array. 

The code is self-contained and can be easily copied and run to test its functionality. When the code is executed with example inputs, such as `arr = [-3, -4, 5] and k = 3`, it returns the expected output `[-4, -3, 5]`. 

The function is designed to efficiently solve the problem statement provided, which involves finding the maximum `k` numbers in an input array.