```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that sorts the array based on the return values of the function. Here we use `lambda` to define an anonymous function that returns the result of the `bin` function applied to the input `x`. The `count` method applied to the result of `bin` gives the number of ones in the binary representation of the number, and the result is sorted in ascending order. In case of a tie, the secondary sorting criterion is the original decimal value of the number `x`.