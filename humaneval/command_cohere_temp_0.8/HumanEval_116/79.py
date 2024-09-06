```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects; in this case, we defined a lambda function `lambda x: (-bin(x).count('1'), x)` which achieves the required sorting as per the problem statement. The `bin` function returns the binary representation of the given number, and the `count` method returns the number of occurrences of the specified element in the string, in this case, '1'. Thus, this function returns a tuple of the number with reversed order and the original number, sorting the array as per the problem statement.