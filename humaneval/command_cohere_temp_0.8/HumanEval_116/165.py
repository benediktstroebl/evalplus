```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting. In this case, the code defines a lambda function that calculates the number of `1` in the binary representation of the number (`bin(x).count('1')`), and then sorts in ascending order. In case of a tie, it sorts based on the decimal value of the numbers.