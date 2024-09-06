```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array. The `sort_array` function then uses a lambda to sort the array by first using the number of ones in descending order and as a secondary measure, sorts lower values to a higher priority than higher values, ensuring that the decimal value is considered when there is no difference in the number of ones.