```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This script employs Python's `count_ones` function to quantify the number of '1's in binary representation, and utilizes `sort` with a custom key to arrange integers according to their binary 'ones' count. Notably, if there's a tie in 'ones' count, the sorting is based on the decimal value in descending order. The script efficiently handles various input scenarios, including negative numbers, and outputs the expected sorted array.