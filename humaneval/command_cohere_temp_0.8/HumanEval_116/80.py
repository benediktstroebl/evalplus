```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This script employs Python's `count_ones` function to tally the number of '1's in binary representation, achieving numerical sorting. The `sort_array` function utilizes this metric, pairing it with negative decimal value sorting to arrange identical ones counts in descending order. The function then returns the sorted array, adhering to the problem's specific guidelines.