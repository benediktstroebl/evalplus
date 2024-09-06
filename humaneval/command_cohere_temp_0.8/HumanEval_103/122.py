Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    total = (n + m) // 2
    count = m - n + 1
    avg = total // count
    return bin(round(avg))[2:]
```

The provided Python script defines a function `rounded_avg` that takes in two integers `n` and `m`, representing the lower and upper bounds of a range of numbers. The function first checks if `n` is greater than `m`, and if so, returns -1. Otherwise, it calculates the average of the numbers in the range using the formula: 
```
(n + m) / 2
```
It then computes the count of numbers in the range `m - n + 1`, and updates the average if necessary. The result is rounded to the nearest integer and converted to binary using the built-in `bin` function. The script returns the binary representation of the rounded average if the input is valid; otherwise, it returns -1.  This solution leverages basic arithmetic and binary conversion techniques to solve the problem in a efficient and concise manner.