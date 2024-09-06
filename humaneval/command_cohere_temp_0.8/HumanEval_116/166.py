```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting. In this case, the code defines a lambda function that calculates the number of `1` in the binary representation of `x` (the first return value) and sorts subsequently sorts them in ascending order.

If there is a tie in the number of ones, it sorts based on the decimal value of the numbers.

This approach uses `bin(x)` which returns the binary representation of the integer `x`. The `count('1')` method returns the number of occurrences of '1' in the binary representation of the number, which corresponds to the number of '1' in its binary representation. 

This approach assumes that the input array contains only valid integers and that there are no duplicate elements, as these cases are not handled by the specification.