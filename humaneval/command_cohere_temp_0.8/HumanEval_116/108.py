```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that returns the parameters for sorting. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` method then sorts the array based on these parameters in ascending order. 

After calling the `sort` method, the result is returned from the `sort_array` function, which is the sorted array based on the specified criteria.