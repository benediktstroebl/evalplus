```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before comparison. Here, the lambda function `lambda x: (bin(x).count('1'), x)` first calculates the number of `1`s in the binary representation of each number `x` (`bin(x).count('1')`) and then returns this value, coupled with the actual value `x`, as a tuple. The list is then sorted in ascending order based on the tuple of returned values.