```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, the function `lambda x: (-bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` function will sort the array according to the tuple in ascending order. 

The `bin` function returns the binary representation of a number as a string. The `count` method returns the number of occurrences of the specified string in the binary representation of the number.