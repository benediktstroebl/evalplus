```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects; in this case, we defined a lambda function `lambda x: (-bin(x).count('1'), x)` which achieves the required sorting as described in the problem. The bin function returns the binary representation of the decimal number. The count of ones is determined using the `count` method, and the numbers are sorted in descending order using the `(-)` operator. Finally, the sorted array is returned.