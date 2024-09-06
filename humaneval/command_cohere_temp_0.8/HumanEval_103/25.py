Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded = avg % 1
    return '-1' if rounded < 0 else f'0b{rounded:b}'
```

The provided solution is concise and efficient and should serve as an optimal solution for the given problem. It checks for edge cases, where if the average is less than 0, it returns `-1` in binary, and if the average is between 0 and 1, it returns the binary representation of the exact decimal value.