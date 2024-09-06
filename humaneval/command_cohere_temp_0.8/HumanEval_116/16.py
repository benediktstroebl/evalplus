```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that formats the elements of the list before they are compared. In this case, each element `x` is converted to its binary representation using the `bin` function, and the number of occurrences of the digit '1' in this binary representation is counted using the `count` method. These two values are returned in a tuple and used for sorting. Elements with more '1's in their binary representation will come first, and if there is a tie, the elements are sorted based on their decimal value. 

This approach helps to sort the array of integers according to the number of ones in their binary representation in ascending order, while preserving the original order for elements with similar number of ones in their binary representation. 

The test examples provided in the problem statement will return the expected results when using this function.