```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that transforms each element in the list. Here, a lambda function `lambda x: (bin(x).count('1'), x)` is used. This function first uses the `bin` function to get the binary representation of each element `x`. The `count('1')` method counts the number of occurrences of '1' in the binary representation. This value is used to break ties and sort the list in ascending order. If the number of '1' counts are the same, then the decimal value of `x` is used as a backup option to maintain consistency. 

The script returns the sorted array as described in the problem statement.