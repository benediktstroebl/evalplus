```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array. The `sort_array` function then sorts the array using the `count_ones` value as the primary key and the decimal value as a secondary key to break ties. The resulting array is then returned.