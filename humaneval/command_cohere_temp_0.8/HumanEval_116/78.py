```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments that the list should be sorted on. In this case, each element `x` in the list is passed to the lambda function `(-bin(x).count('1'), x)`.

The lambda function counts the number of occurrences of '1' in the binary representation of the number. The number is first converted to binary using the `bin` function. The resulting string is split into a list of digits, and then the list of digits is counted. The lambda function returns a tuple of (-count, x) where count is the number of ones in the binary representation of the number, and x is the number itself.

The `sort` function sorts the list according to the lambda function. The numbers with more binary ones will appear first, and if there is a tie, the numbers will be sorted according to their decimal value in ascending order.