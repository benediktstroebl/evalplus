```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before sorting. Here, the lambda function `lambda x: (-bin(x).count('1'), x)` is used.

The `bin` function returns the binary representation of a number as a string. The `count('1')` method returns the number of occurrences of '1' in the binary representation. This value is negated and used to sort the list in descending order. If the number of '1' is the same, then the decimal value is used to sort the list in ascending order.