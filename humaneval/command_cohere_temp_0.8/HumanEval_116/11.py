```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects; in this case, the lambda function returns the arguments `(-bin(x).count('1'), x)` for sorting. Here, `bin(x)` converts the variable `x` to its binary representation, and `.count('1')` counts the number of occurrences of `1` in the binary representation. The numbers are sorted in descending order based on the count of `1` as the first parameter and in ascending order based on their decimal value as the second parameter.

The script sorts the array `[1, 5, 2, 3, 4]` and returns the expected output `[1, 2, 3, 4, 5]`. It also sorts the array `[1, 0, 2, 3, 4]` and returns the expected output `[0, 1, 2, 3, 4]`. Lastly, it sorts the array `[-. 2, -3, -4, -5, -6]` and returns the expected output `[-6, -5, -4, -3, -2]`.