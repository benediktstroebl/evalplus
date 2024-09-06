```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that can be used to transform the elements being compared. In this case, the function `lambda x: (bin(x).count('1'), x)` first calculates the number of `1`s in the binary representation of each element `x` and then returns this value, paired with the element itself, as a tuple. The `sort` function then compares these tuples and sorts the array accordingly.