```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting. In this case, for every element `x` in the array, the lambda function returns a tuple where the first element is the number of ones in the binary representation of `x` obtained from the `bin(x).count('1')` expression, and the second element is `x` itself. The array is then sorted according to this tuple in ascending order.