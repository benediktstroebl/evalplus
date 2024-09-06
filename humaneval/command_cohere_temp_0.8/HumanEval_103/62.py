Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```

The provided example uses the formula for computing the average `((n+m)/2)` and checks if `n > m` to return `-1` if necessary. The function then rounds the average using the `round()` function and converts it to binary using the `bin()` function.