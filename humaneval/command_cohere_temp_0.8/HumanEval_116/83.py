```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, we define a lambda function that calculates the number of '1's in the binary representation of an integer `x` using the `bin` function, and then sorts the list first by the count of these '1's in ascending order, and then by the decimal value of the numbers in case of a tie.