```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments to be used for sorting. In this case, for every number in the array, the lambda function returns a tuple where the first element is the number of '1's in the binary representation of the number and the second element is the number itself. The numbers are then sorted based on the first element of the tuple, and if the first elements are equal, they are sorted based on the second element.