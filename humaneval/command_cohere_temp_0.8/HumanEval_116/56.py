```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects; in this case, the lambda function `lambda x: (-bin(x).count('1'), x)` achieves the desired effect. This function converts each element `x` to a binary string `bin(x)` and counts the number of occurrences of '1' in that string. The result is reversed to achieve the desired order, with the highest number of ones first, and elements with the same number of ones sorted in decimal order. 

The script returns the correctly sorted array according to the given problem statement.