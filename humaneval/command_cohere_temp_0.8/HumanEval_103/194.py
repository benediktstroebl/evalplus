Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded_avg = bin(round(avg)).replace('0b', '')
    return rounded_avg
```
The code snippet provided calculates the average of the given integers (`n` and `m`) and rounds it to the nearest integer. It then converts the rounded average to binary and returns the result. If `n` is greater than `m`, it returns `-1`. Feel free to test this code with different inputs to verify its behavior.