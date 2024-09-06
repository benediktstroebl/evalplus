```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that does custom sorting. Here, a lambda function `lambda x: (bin(x).count('1'), x)` is used where `bin(x)` returns a string representing the binary representation of `x`, and `.count('1')` gives the number of ones in that binary representation. If the number of ones is the same, the decimal value of `x` will break the tie. The sorted array is then returned. 

This function uses these ideas to sort the array `arr` according to the number of ones in their binary representation in ascending order, while maintaining the original order for entries with the same number of ones. 

> **NOTE**: Using `bin(x)` will return a binary string representing the absolute value of `x` as `[1]` is not included in the input. To include `[1]` in the sorted output, an alternate approach could be used such as converting to and from base 10.