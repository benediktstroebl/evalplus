Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    sum_ = sum(range(n, m + 1))
    avg = round(sum_ / (m - n + 1))
    return bin(avg)[2:]
```

The function `rounded_avg` takes in two positive integers `n` and `m` and computes the average of the integers from `n` through `m` (including `n` and `m`). It then rounds the average to the nearest integer and converts it to binary. 

The condition `if n > m` checks if the passed `n` value is greater than `m`, and if so, returns -1 as per the problem's instructions. 

The sum of the range is calculated using the sum function and range from `n` to `m` (inclusive), and the average is computed by dividing this sum by the number of elements in the range (`m - n + 1`), then rounded using the round function. 

Finally, the result is converted to binary by taking the binary representation of the integer using `bin`, and returning the binary string from index 2 onwards (as per the function's instruction to return the binary string). 

This code will provide the desired binary string for valid inputs, or -1 for invalid ones, following the problem's specification.