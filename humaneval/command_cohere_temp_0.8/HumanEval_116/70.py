```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that returns the parameters for sorting the list. In this case, we define a lambda function `lambda x: (bin(x).count('1'), x)` which first counts the number of '1's in the binary representation of each number `x` and then sorts them in ascending order if the number of '1's is the same, thus ensuring the required solution.