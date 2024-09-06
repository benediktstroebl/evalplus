```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in the binary representation of a given number. The `sort_array` function uses a custom sorting key that first compares elements based on their binary ones count in ascending order and then, for elements with the same number of ones, sorts them in descending order based on their decimal value.