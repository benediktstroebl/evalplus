Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    diff = m - n 
    avg = (n + m) // 2 
    binary = bin(avg)[2:] 
    if diff < 0 or diff % 2 == 0:
        return binary
    else:
        return -1
```
This function calculates the average of numbers from `n` to `m`, rounds it to the nearest integer, and then converts it to binary. If `m - n` is negative or an even number, it returns the binary number, but if it's odd, it returns -1, as per the problem statement.