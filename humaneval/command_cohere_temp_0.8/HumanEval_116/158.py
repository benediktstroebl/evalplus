```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in the binary representation of a given number. The `sort_array` function uses a lambda to sort the array using the calculated number of ones as the primary key and the decimal value as the secondary key to sort similarly numbered ones.