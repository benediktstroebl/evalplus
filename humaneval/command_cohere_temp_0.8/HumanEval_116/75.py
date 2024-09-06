```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects; in this case, the lambda function returns the parameters `(-bin(x).count('1'), x)` for sorting. The `bin` function returns the binary representation of `x`, and the `count` method returns the number of occurrences of `1` in the binary representation. The result is sorted in ascending order based on the number of `1`s in the binary representation of the numbers. For numbers with the same number of ones, it sorts based on the decimal value.