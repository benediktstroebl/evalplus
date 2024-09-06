```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments that the list should be sorted on. In this case, each value `x` in the list is passed to the lambda function `(-bin(x).count('1'), x)`. The first argument of the lambda function executes the following:
```python
bin(x)
```

Which converts the decimal number to a binary string and returns the number of ones in the binary representation of the decimal number. The lambda function returns a tuple of the number of ones and the value of `x` and will sort in ascending order. Values with more ones will come first and if there is a tie, it will sort based on the decimal value as specified in the prompt.