```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This script employs the `count_ones` function to tally the number of '1's in the binary representation of every number, and then sorts the array primarily by this count, and secondarily by decimal value in case of a tie.