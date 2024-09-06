```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before sorting. Here, a lambda function `lambda x: (-bin(x).count('1'), x)` is used. 

The `bin` function converts the elements to their binary representation. The `count('1')` method counts the number of occurrences of '1' in the binary representation. This value is negated to ensure that elements with more '1's appear first. In the case of a tie, the original decimal value is used as a secondary sorting criterion.

This approach results in the desired sorting order as specified in the problem statement.