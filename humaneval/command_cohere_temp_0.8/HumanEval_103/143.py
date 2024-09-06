Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    diff = m - n
    if diff > 0 or (diff == 0 and m == n):
        return "-1"
    avg = (n + m) // 2
    return f"0b{bin(round(avg))[2:]}"
```

The script defines a function `rounded_avg` that takes in two integers `n` and `m` as parameters. If `m` is less than `n`, it returns `-1`. If not, it calculates the average of the two numbers and rounds it to the nearest integer. The rounded value is then converted to binary and returned as a string.

The function is designed to be self-contained, meaning that it does not rely on any external variables or functions other than those included in the function itself. It is reusable and can be imported and used as a module in other Python scripts.