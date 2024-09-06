```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array, and the `sort_array` function uses a lambda to sort the array using the desired logic, non-negative integers with more ones first, and then decimal value as a secondary sort key.