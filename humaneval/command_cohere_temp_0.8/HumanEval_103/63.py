Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```
This function takes two integers `n` and `m` as input and returns the binary representation of the average of the integers between them if `n` is less than or equal to `m`, or `-1` if `n` is greater than `m`. The `round()` function is used to round the average to the nearest integer, and `(bin(x)[2:])` is used to convert the rounded integer to its binary representation, as specified in the prompt.