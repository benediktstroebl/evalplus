```python
def count_ones(n):
    return bin(n).count("1")

def sort_array(arr):
    arr.sort(key=lambda n: (count_ones(n), -n))
    return arr
```

This Python script solves the problem as described in the prompt. The `count_ones` function calculates the number of ones in the binary representation of each number, and the `sort_array` function uses a lambda to sort the array first by the ones count and then by the decimal value in descending order in case of a tie.