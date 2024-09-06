Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = (n + m) // 2
    return bin(round(avg))[2:]
```
This script defines a function `rounded_avg` that takes in two integers `n` and `m` and returns the binary representation of the average of the two numbers rounded to the nearest integer if they are in the correct order, and returns -1 if `n` is greater than `m`.  The `round` function is used to round the average to the nearest integer, and the `bin` function converts the result to binary. The returned binary number is then truncated to exclude the '0b' prefix by using `[2:]`. 

Here is an example usage of the function:
```python
rounded_avg(1, 5)
```
This would return the string "0b11", as the average of 1 and 5 rounded to the nearest integer is 3, which in binary form is "011". 

This approach takes advantage of Python's built-in rounding and binary conversion methods.