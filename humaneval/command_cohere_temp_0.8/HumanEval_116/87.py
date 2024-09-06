```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that tells the sorting function how to compare each pair of elements. The lambda function `lambda x: (bin(x).count('1'), x)` first calculates the number of `1` in the binary representation of number `x`, and in case of a tie, it sorts according to the decimal value of the number.