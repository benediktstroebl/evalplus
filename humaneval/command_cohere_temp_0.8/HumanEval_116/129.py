```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in the binary representation of a given number. It also defines the `sort_array` function, which sorts the array based on the number of ones in the binary representation in ascending order. If the number of ones is the same, it sorts them based on their decimal value in descending order. The code uses the `key` parameter in the `sort` method to define a custom sorting function that combines both the number of ones and the decimal value of the numbers.