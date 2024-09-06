```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

The `count_ones` helper function calculates the number of ones in the binary representation of each number in the array, and the `sort_array` function uses a lambda to sort the array according to the number of ones in the binary representation in ascending order, and then, if there is a tie, it sorts based on the decimal value in descending order.