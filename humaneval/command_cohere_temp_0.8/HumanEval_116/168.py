```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects. In this case, the lambda function `lambda x: (-bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` function will first sort the array according to the number of ones in their binary representation in ascending order, and then in the case of similar number of ones, it will sort based on the decimal value of the numbers. 

The `bin` function returns the binary representation of the given number as a string. The `count` method returns the number of occurrences of the specified element in the string (in this case, the string is the binary representation of the number), so `bin(x).count('1')` returns the number of ones in the binary representation of the number. 

This function returns the sorted array as described in the problem statement.