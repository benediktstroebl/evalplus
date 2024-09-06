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

The script provides the average of the integers between `n` and `m`, rounds it to the nearest integer, and returns the binary representation. It ensures correctness by checking if `n` is greater than `m` and handling the case where the two integers are misordered.