```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, we define a lambda function that calculates the number of '1' counts in the binary representation of an integer `x` using `bin(x)` and `count('1')`, and returns the integer `x` itself as the second parameter. These parameters make the function sort the array according to the number of ones in their binary representation in ascending order, and in the event of a tie, it will sort based on the decimal value of the numbers. The resulting sorted array fulfills the problem requirements.