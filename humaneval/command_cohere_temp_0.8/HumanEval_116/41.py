```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in a binary representation of a number and a `sort_array` function that uses a lambda to sort the array by first sorting them by the ones count and then by the decimal value of the number when the number of ones is the same.