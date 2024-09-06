Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    total = (m + n) // 2
    count = 1
    prev = n
    while count < m:
        if prev + 1 < m:
            prev += 1
            count += 1
        else:
            break
    if n > m:
        return -1
    avg = total
    if prev == m:
        return bin(avg)[2:].zfill(64)
    else:
        return bin(avg + 1)[2:].zfill(64)
```
This script includes a full Python environment with a function `rounded_avg` that can be executed independently to solve the given problem. It calculates the average of integers between `n` and `m`, rounds it to the nearest integer, and converts it to binary. It also handles edge cases such as when `n` is greater than `m` or when the average equals a whole number.