Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) // 2
    return bin(round(avg))[2:]
```

The provided Python script solves the problem using a straightforward approach. It first checks if `n` is greater than `m` and returns -1 if this inequality is true, as per the problem's guideline. If `n` is not greater than `m`, it calculates the average of the two values and rounds it to the nearest integer. Finally, it converts the rounded average to a binary string, which is the return format specified in the problem.