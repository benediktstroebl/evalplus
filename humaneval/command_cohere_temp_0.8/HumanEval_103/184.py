Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```
This function accepts two positive integers `n` and `m` as inputs and returns the binary representation of the result of rounding the average of the integers from `n` through `m` to the nearest integer. It handles the case where `n` is greater than `m` by returning -1. 

The rounding is done using Python's built-in `round` function, and the binary representation is obtained by using the `bin` function. The `[2:]` slice is used to remove the leading '0b' from the result.