Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0: 
        return -1 
    elif len(binary) & 1: 
        return int(binary, 2) 
    else: 
        return int(binary[0])
```
This script defines a function `rounded_avg` taking two integers `n` and `m` as input, and it computes the average of these numbers and returns the result converted to binary. If `n` is greater than `m`, it returns -1.