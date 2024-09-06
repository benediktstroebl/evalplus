Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    diff = m - n
    avg = (n + m) // 2
    rounded_avg = (-1 if diff < 0 else bin(avg)[2:].rjust(32, '0'))
    return rounded_avg
```
This function handles the edge case where `m` is greater than `n` by returning -1. It also performs binary conversion using the `bin` function and right justification with zeros to ensure a 32-bit binary string. Feel free to test this function with the examples provided in the problem statement, and it should produce the expected outputs.