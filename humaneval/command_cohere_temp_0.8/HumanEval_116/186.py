```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the arguments that the list should be sorted by, in this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the variable `x`, and the second element is `x` itself. The list is sorted by the number of ones in the binary representation in ascending order and remains sorted by decimal value for values with the same number of ones. The function correctly returns the input list sorted accordingly, as specified in the challenge statement.