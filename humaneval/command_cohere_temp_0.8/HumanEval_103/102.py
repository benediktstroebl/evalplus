Here's a Python script with a self-contained function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    total = (n + m) // 2
    count = m - n + 1
    avg = total // count
    return bin(round(avg))[2:]
```

The provided Python script solves the problem using the midpoint of the range of numbers. It first checks if the `n` value is greater than `m`, and if so, it returns `-1` as the binary string. Otherwise, it calculates the average of the integers in the range using the formula: `(n + m) // 2`, which calculates the midpoint and counts the number of integers in the range using `m - n + 1`. It then rounds the average to the nearest integer and converts it to a binary string, following the format specified in the example test cases.