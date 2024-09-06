```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of occurrences of 1 in the binary representation of each number in the array. The `sort_array` function then uses a lambda to sort the array according to the number of ones in the binary representation in ascending order and, in case of a tie, sorts the numbers by their decimal value in descending order.