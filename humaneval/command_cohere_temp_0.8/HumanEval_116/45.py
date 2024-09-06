```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting the list. In this case, the function `lambda x: (-bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `-` before the `bin` repository is used in python to introduce negation. Hence, the sorting is done in descending order of ones in binary representation and ascending order of the decimal value for similar ones-count values. 

The script returns the sorted array according to the specified criteria.