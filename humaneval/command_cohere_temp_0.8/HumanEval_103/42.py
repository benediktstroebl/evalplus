Here's a Python script with a self-contained function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    bin_str = '{0:b}'.format(((n + m) // 2))
    return bin_str if n <= m else -1
```

The function directly computes the average of the integers between `n` and `m`, rounds it to the nearest integer, and then converts it to binary. If `n` is greater than `m`, it returns `-1` as specified in the prompt.