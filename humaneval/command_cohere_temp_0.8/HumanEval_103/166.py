Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```

The provided Python script solves the problem using a straightforward approach. It first calculates the average of the integers between `n` and `m`, inclusive, using the formula `(n + m) // 2`. Then, it checks if `n` is greater than `m` and returns -1 if so, as specified in the problem statement. Lastly, the script applies the `round()` function to round the average to the nearest integer and converts it to binary using the `bin()` function. The resulting binary string is returned, excluding the '0b' prefix. 

This script efficiently computes the rounded average and returns the result in binary format, adhering to the problem constraints.