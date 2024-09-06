Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```
The script offers a concise way to compute the average of integers between `n` and `m`, round it, and then represent it in binary form. If `n` is greater than `m`, it returns -1.