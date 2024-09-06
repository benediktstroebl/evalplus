Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    """
    Compute the average of integers from n to m (inclusive), round to the nearest integer, 
    and convert to binary. Returns -1 if n > m.
    """
    if n > m:
        return -1
    total = (n + m) // 2  # Average is the midpoint between n and m
    return format(round(total), 'b')
```

This script defines a function `rounded_avg` that takes in two positive integers `n` and `m` and returns the binary representation of the rounded average of the integers from `n` to `m` (inclusive). If `n` is greater than `m`, it returns `-1`. The `round` function is used to round the average to the nearest integer, and the `format` function is used to convert the rounded average to binary.