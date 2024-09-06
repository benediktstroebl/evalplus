```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting the list. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple containing the number of ones in the binary representation of the number and the number itself. The numbers are sorted based on the number of ones in their binary representation in ascending order. If the number of ones is the same, they are sorted based on their decimal value in ascending order.