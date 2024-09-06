```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments that the list should be sorted by, in this case, a lambda function `lambda x: (bin(x).count('1'), x)` which returns the number of `1` in the binary representation of the number and the number itself. The `sort` function will sort the list based on these return values. Ascending order is ensured by placing the number of ones in the binary representation first in the tuple. The function works in both cases where the integers are positive and negative.