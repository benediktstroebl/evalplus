```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments that the list should be sorted by, in this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple containing the number of occurrences of '1' in the binary representation of the variable `x` and `x` respectively. The list is sorted by the number of `1`s in the binary representation in ascending order and if there is a tie, it is sorted by the decimal value of the numbers. 

The Python script efficiently implements the specified sorting algorithm and achieves the desired output for the given examples in the problem statement.