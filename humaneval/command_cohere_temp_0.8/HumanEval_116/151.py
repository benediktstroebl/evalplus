```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that transforms each element in the list before sorting. Here, a lambda function `lambda x: (bin(x).count('1'), x)` is used. This function first converts the element `x` to its binary representation using `bin(x)`. It then counts the number of occurrences of '1' in this binary representation using `bin(x).count('1')`. This number of '1's is used for sorting in ascending order. If the number of '1's is the same for two elements, then the decimal value of `x` is used as a tiebreaker. 

The script returns the sorted array as described in the problem statement.