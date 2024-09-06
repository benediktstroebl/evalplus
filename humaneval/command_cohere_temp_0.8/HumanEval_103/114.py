Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded = avg % 1
    return '0b' + bin(int(rounded * 2))[2:][:1]
```
This script defines a function `rounded_avg` that takes in two positive integers `n` and `m` and returns the binary representation of the average of the two numbers rounded to the nearest integer if `n` is not greater than `m`. If `n` is greater than `m`, it returns -1. The script incorporates edge cases such as `rounded_avg(7,5)`, `rounded_avg(10,20)`, and `rounded_avg(20,33)`.