```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that determines the sort order. In this case, for every element `x` in the array, the lambda function returns a tuple `(bin(x).count('1'), x)`, where `bin(x)` gives the binary representation of `x`, and `.count('1')` gives the number of ones in that binary representation. Elements with more significant digits (more ones) come first, and if the number of ones is the same, the decimal value determines the order. The resulting array is sorted according to this specification, as required by the problem statement.