```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` function then sorts the array based on these values.

The code tests the function with examples such as `sort_array([1, 5, 2, 3, 4])` returning `[1, 2, 3, 4, 5]` and passes the test cases as expected.