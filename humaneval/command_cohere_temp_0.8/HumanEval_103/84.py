Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    total = (n + m) // 2
    count = m - n + 1
    avg = total // count
    return bin(round(avg))[2:]
```
This function handles the edge case where `n` is greater than `m` by returning -1. It also calculates the average of the integers between `n` and `m`, inclusive, and rounds the average to the nearest integer before converting it to binary.