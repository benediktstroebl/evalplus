```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` function will sort the array based on these parameters in ascending order. 

The code satisfies the given requirements and fulfills the expected outputs for the provided examples. To implement this code in Jupyter Notebook or in a Python script, the corresponding test cases should be defined and used to verify the correctness of the function.