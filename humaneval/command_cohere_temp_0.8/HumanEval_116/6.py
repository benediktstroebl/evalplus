```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that defines the sort order. In this case, the function `lambda x: (-bin(x).count('1'), x)` returns a tuple containing two criteria for sorting:
1. Sort arrays in descending order based on the number of ones in the binary representation of each number. This is achieved by counting the number of occurrences of '1' in `bin(x)` for each element `x` in the list. 

2. If the number of ones is the same, sort the arrays in ascending order based on the decimal value of the numbers.

This will ensure that the array is sorted according to the specified criteria, as required by the prompt.