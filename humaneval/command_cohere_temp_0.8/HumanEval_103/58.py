Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded_avg = bin(round(avg)).replace('0b', '')
    return rounded_avg
```

The provided example uses the `round` function to achieve the rounding behavior as described in the problem statement. The function returns the binary string for this rounded value. When `n` is greater than `m`, the function returns `-1`.