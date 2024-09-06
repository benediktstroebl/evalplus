```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting the list. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The numbers are sorted based on the first element of this tuple, and if the first element is the same, then the second element is considered. 

The test cases provided in the problem statement return the expected output when the `sort_array` function is applied, validating the correctness of the function. 

This approach leverages Python's powerful `lambda` and `bin` functions to effectively solve the problem.