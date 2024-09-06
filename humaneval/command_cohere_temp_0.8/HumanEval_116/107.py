```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` function then sorts the array based on these values.

The tests provided in the problem statement ensure that the function `sort_array` sorts the array according to the specified criteria. 

If you would like to test this function with more examples, you can add additional test cases to confirm its correctness.