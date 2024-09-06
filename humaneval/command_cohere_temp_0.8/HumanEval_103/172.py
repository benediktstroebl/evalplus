Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    bin_str = '-1' if n > m else bin(round((n + m) / 2))[2:]
    return bin_str if n <= m else -1
```
This script provides a function that solves the problem as outlined in the example test cases provided. The function `rounded_avg` takes in two positive integers `n` and `m` and returns the binary representation of the result after rounding the average to the nearest integer. The function handles the case where `n` is greater than `m` by returning `-1`.