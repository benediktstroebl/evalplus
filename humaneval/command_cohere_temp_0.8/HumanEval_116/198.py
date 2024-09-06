```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array. The `sort_array` function then sorts the array using the `count_ones` value as the sorting key, ensuring that numbers with the same number of ones are sorted in decimal order. The resulting sorted array meets the specified expectations.