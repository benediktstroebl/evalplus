Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    return bin(round(avg))[2:]
```
This script defines a Python function `rounded_avg` that takes in two positive integers `n` and `m` and returns the binary representation of the average of integers from `n` through `m`, rounded to the nearest integer, or -1 if `n` is greater than `m`.

The `round` function is used to round the average calculated by summing and dividing `n` and `m` to the nearest whole number. To handle the rounding and conversion to binary, the `bin` function is utilized in the code. Lastly, the condition `if n > m` is applied to identify the scenario of `n` being greater than `m`, which is a requirement mentioned in the problem statement. 

You can use this code to implement the function rounded_avg and utilize it to solve the given problem. Feel free to adapt this response to fit your needs or ask if you have any questions!