Here's a Python script that includes a function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    num = (n + m) // 2
    bin_str = bin(round(num))[2:]
    return bin_str if len(bin_str) <= len(str(max(n, m))) else "-1"
```

This function handles the edge cases and returns the correct binary string for the given range of integers.