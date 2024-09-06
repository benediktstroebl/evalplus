```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that determines the sort order of each element. In this case, a lambda function is used to calculate the number of '1' in the binary representation of each element and its decimal value as a secondary key to determine the final sort order.