```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that formats the elements before comparison. Here, each element `x` is first passed through the lambda function `lambda x: (bin(x).count('1'), x)`. This function first counts the number of ones in the binary representation of `x` and then, in case of a tie, returns the actual value of `x`. The result is that the array is sorted in the required manner.