```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` function calculates the number of ones in the binary representation of a given number, and the `sort_array` function uses a custom sorting key that first compares elements based on their count of ones in binary form, and then resorts to the decimal value as a tie-breaker, sorting in ascending order.