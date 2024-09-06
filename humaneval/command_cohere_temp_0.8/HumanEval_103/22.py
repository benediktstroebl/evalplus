Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded_avg = round(avg)
    return bin(rounded_avg)[2:]
```

The provided example uses the `round` function to round the average computed (`(n+m)//2`) to the nearest integer. The `bin` function converts the rounded integer to a binary string, and the `[2:]` slice is used to remove the leading '0b'. This produces the desired binary string output.