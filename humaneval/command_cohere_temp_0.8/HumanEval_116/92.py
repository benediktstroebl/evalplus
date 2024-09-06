```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The code defines a `count_ones` function that calculates the number of occurrences of `1` in the binary representation of a number. The `sort_array` function then uses a lambda to sort the array using the calculated number of ones as the primary key and the decimal value as the secondary key to break ties.