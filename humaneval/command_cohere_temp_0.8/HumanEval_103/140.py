Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```

The provided example uses the binary operator `//` to perform integer division, which returns the floor value of the division operation. To achieve a rounded average, it is essential to incorporate rounding by utilizing the `round()` function. The `round()` function approximates a given number to the nearest whole number or integer.

In the case where `n` exceeds `m`, the function promptly returns `-1`. This distinct case handling guarantees that the function adopts a consistent behavior for invalid input scenarios. 

The function concludes by extracting the binary representation of the rounded average using the `bin()` function. Specifically, the `bin()` function converts the result of `round(avg)` to a binary string, and the `[2:]` slice is applied to remove the leading '0b' or '0B'. 

This code achieves the desired output format of a binary string for the problem statement.