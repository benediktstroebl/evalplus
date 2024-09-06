```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before comparison. Here, the lambda function `lambda x: (bin(x).count('1'), x)` first calculates the number of `1`s in the binary representation of each element `x` and then returns this value together with `x` as a tuple. Elements are first compared by the number of `1`s in their binary representation and then, if the number of `1`s is the same, by their decimal value. 

The code implements the specified test cases and any other query dealing with non-negative integers' sorting according to the number of ones in their binary representation.  This approach will work correctly for positive integers only.