```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This code defines a `count_ones` function that calculates the number of ones in the binary representation of a given number. It also defines the `sort_array` function, which sorts the array based on the result of the `count_ones` function. In case of a tie, the decimal value is used as a tie-breaker.