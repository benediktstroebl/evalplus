```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting. In this case, the code defines a lambda function that calculates the number of `1` in the binary representation of `x` (the first criterion), and if it is a tie, it sorts according to the decimal value of `x` (the second criterion). 

This approach achieves the required sorting order specified in the problem statement.