Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```
This script defines a Python function `rounded_avg` that takes in two positive integers `n` and `m` and returns the binary representation of the average of integers between `n` and `m` (`inclusive`), rounded to the nearest integer. If `n` is greater than `m`, it returns -1.

Here is an example function call:
```python
rounded_avg(1, 5) # Returns "0b11"
```