```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, we define a lambda function that calculates the number of `1`s in the binary representation of an integer `x` and returns this number together with `x`. Hence, the list is sorted first according to the number of `1`s in the binary representation and then according to the decimal value of the numbers for elements with similar number of `1`s. The desired output is achieved accordingly.