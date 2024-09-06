```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This script employs the `count_ones` function to tally the number of `1`s in the binary representation of each number in the array, and then sorts the array based on this count. When the counts are alike, the numbers are ordered by their decimal value in descending order.