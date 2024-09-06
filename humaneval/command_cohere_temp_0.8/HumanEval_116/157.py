```python
def count_ones(n):
    return bin(n).count('1')

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This Python script solves the problem as described in the markdown code block. It first defines a helper function `count_ones` that calculates the number of ones in the binary representation of a given number `n`. Then, the `sort_array` function uses a lambda to sort the array using the desired criteria, first based on the count of ones in the binary representation and then, for numbers with the same number of ones, it sorts based on the decimal value in descending order.