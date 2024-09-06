```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that does custom sorting. In this case, for every number in the array, the lambda function `lambda x: (bin(x).count('1'), x)` is executed. It first converts the number to a binary string and counts the number of occurrences of "1" in the string (`bin(x).count('1')`), which corresponds to the number of ones in the binary representation. If the count is the same for two numbers, the second part of the lambda function sorts them by their decimal value in ascending order.