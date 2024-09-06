```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments passed to the sorting function as a tuple. In this case, the lambda function `(-bin(x).count('1'), x)` achieves the desired result. The bin function converts an integer to a binary string, and the count '1' argument returns the number of ones in the binary representation of the number. The numbers are sorted in descending order, and finally, the sorted list is returned from the function.