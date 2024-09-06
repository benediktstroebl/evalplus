```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The function `count_ones` is used to calculate the number of ones in the binary representation of each number in the array, and the `sort_array` function uses a custom key to sort the array first by the number of ones in descending order and then by the decimal value in ascending order.