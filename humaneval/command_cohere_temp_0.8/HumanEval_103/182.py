Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    bin_str = [-1 if i == 0 else '0' for i in range(m - n + 1)]
    if n > m:
        return -1
    for i in range(n, m + 1):
        bin_str[i - n] = str(bin(i % 2 + 1))[2:]
    s = ''.join(bin_str)
    return '0b' + ('1' if int(s) % 2 else '') + s[::-1] if s else '0b0'
```
This script provides a binary representation of the average of integers adjusted to the nearest integer, handling edge cases as specified in the problem statement.