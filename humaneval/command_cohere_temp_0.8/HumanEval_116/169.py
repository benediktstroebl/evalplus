```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, we define a lambda function that calculates the number of `1` in the binary representation of an integer `x` and returns it, and then returns `x` as the secondary parameter in case of ties. The array is sorted based on this key, ordering first based on the number of ones in the binary representation of the number, and then secondary by the decimal value of the number. 

The script sorts the input array `arr` in accordance with the problem statement and returns the sorted array.