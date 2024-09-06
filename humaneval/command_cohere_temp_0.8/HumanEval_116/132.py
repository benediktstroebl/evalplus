```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, the function `lambda x: (-bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` function will first sort the list based on the first element of the tuple, and then for similar first elements, it will sort based on the second element of the tuple. The final sorted list is returned from the `sort_array` function.

This approach solves the problem by first sorting the array in ascending order based on the number of ones in their binary representation. If the number of ones is the same, it then sorts the array in ascending order based on the decimal value of the numbers.