Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```
This script defines a Python function `rounded_avg` that takes in two positive integers `n` and `m` and returns the binary representation of the average of the two integers rounded to the nearest integer if `n` is not greater than `m`. If `n` is greater than `m`, it returns -1. 

The `round` function is used to round the average to the nearest integer and the `bin` function converts the result to binary. The last two characters `[]` are used to return the binary string without the '0b' prefix.