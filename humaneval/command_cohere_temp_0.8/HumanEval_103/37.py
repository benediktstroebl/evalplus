Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```

The script provides a function that takes two integers `n` and `m` as parameters. It computes the average of these two numbers and rounds it to the nearest integer. Then, it converts the result to binary and returns it if it's within the range of `n` and `m`. Otherwise, it returns `-1`.