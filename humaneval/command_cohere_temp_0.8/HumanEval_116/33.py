```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that sorts the array based on the return values of the specified function. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element counts the number of ones in the binary representation of the variable `x`, and the second element is the decimal value of `x`. By sorting the array based on this tuple, the problem is solved and the tests are satisfied. 

Would you like to know more about the `key` argument or other advanced Python concepts? Feel free to ask!