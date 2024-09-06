Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    avg = (n + m) // 2
    if n > m:
        return -1
    rounded = avg % 1
    binary = bin(rounded)[2:]
    return binary if binary else '0b0'
```

The script provides a function that:
- Calculates the average of numbers from `n` to `m` and rounds it to the nearest integer.
- Checks if `n` is greater than `m`, and returns -1 if it is.
- Converts the rounded average to binary and returns it if it's not zero. 
- Returns '0b0' if the rounded average is zero to avoid returning an empty string. 

The script aligns with the problem statement and example provided in the initial request. 

You can test this function by calling it with different input values to see the resulting binary strings.