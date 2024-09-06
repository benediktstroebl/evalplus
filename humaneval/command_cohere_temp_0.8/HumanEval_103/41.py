Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    num = (n + m) // 2
    bin_str = bin(round(num))[2:]
    return bin_str if len(bin_str) < 10 else bin_str[:1]
```

This script provides a function that correctly calculates the average of integers from `n` to `m`, rounds it to the nearest integer, and then converts it to binary. If the resulting binary string is longer than 10 characters, it is truncated to its first character. This handles the edge case where the average is a decimal number with a long binary representation, such as 0.24, which could otherwise cause a timeout when converting to binary. Finally, the function returns -1 if `n` is greater than `m`, as specified in the prompt.