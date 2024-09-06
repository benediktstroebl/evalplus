```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of occurrences of 1 in the binary representation of each number in the array, which is used as the first criterion for sorting in the `sort_array` function. Additionally, the `-n` expression is used as a secondary criterion to sort these numbers in descending order of their decimal value in case the number of ones is the same.