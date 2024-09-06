Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    if n > m:
        return -1
    while count <= m - n + 1:
        total += count
        count += 1
    rounded = round(total / (m - n + 1))
    if rounded == 0:
        return "0b0"
    binary = bin(rounded)[2:]
    return binary if binary[:1] == '1' else binary[1:]
```

The script provides a function that solves the problem using only the two given integers `n` and `m` and returns the result in binary by applying the specified logic and without using global variables or external imports. It also handles the case where the average is zero by returning "0b0" and correctly rounds the average to the nearest integer.