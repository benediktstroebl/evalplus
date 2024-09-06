```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments passed to the sorting function as a tuple. In this case, the lambda function `(-bin(x).count('1'), x)` achieves the desired effect. `bin(x)` converts the numbers to their binary representation, and `.count('1')` gives the number of ones in the binary representation. The numbers are sorted in descending order based on this count, and lastly, the decimal value is used to break ties. 

This solution provides a quick and efficient way to sort the array of numbers according to the given problem statement.