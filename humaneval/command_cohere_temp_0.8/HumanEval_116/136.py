```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that formats the elements of the list before they are compared. In this case, the function `lambda x: (-bin(x).count('1'), x)` returns a tuple containing two elements. The first element is the number of ones in the binary representation of the number, and the second element is the number itself. The `(-)` operator is used to negate the result of `bin(x).count('1')` so that the number of ones in the binary representation is in descending order. 

The `sort` function will then sort the list according to the returned tuple in ascending order, and the resulting list will be sorted according to the specified logic.