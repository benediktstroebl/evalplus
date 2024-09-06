```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that determines the sorting order. In this case, each element `x` in the list is converted to a binary string using the `bin` function. The number of occurrences of the character '1' in this binary representation is calculated using the `count` method. These counts are used to sort the list in ascending order. If the number of ones is the same, then the decimal value of the elements is used to sort the list.