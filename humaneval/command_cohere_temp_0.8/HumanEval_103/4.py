Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    if n > m:
        return -1
    sum_ = sum(range(n, m + 1))
    avg = round(sum_ / (m - n + 1))
    return bin(avg)[2:]
```

The function `rounded_avg` takes in two positive integers, n and m, and returns the binary representation of the average of the integers from n to m, rounded to the nearest integer, or -1 if n is greater than m. 

The script returns the binary representation of the average using the `bin` function, which returns a string representation of the number's binary value. The `[2:]` slice is used to remove the leading '0b' from the result.