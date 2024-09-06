Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```
This script defines a function `rounded_avg` that takes in two positive integers `n` and `m` and returns the binary representation of the average of the two integers rounded to the nearest integer if `n` is not greater than `m`. If `n` is greater than `m`, it returns -1. This is done using Python's built-in `round` function to round the average to the nearest integer and the `bin` function to convert the result to binary.