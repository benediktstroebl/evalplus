```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in the binary representation of a given number. The `sort_array` function then uses a lambda to sort the array by first using the result of the `count_ones` function as the key to sort and then, as a secondary key, it sorts in descending order to ensure that numbers with the same number of ones in their binary representation are sorted based on their decimal value.