Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the rounded average to binary
    binary_avg = bin(rounded_avg)[2:]
    
    # Return -1 if n is greater than m
    if n > m:
        return -1
    
    return binary_avg
```

The given Python script provides a standalone function `rounded_avg` that accepts two integers `n` and `m` as parameters. This function initially computes the average of the two values and rounds it to the nearest integer. Subsequently, it converts the rounded average to a binary string by extracting the two least significant digits from the binary representation and returns it. If `n` is greater than `m`, the function returns `-1` as the binary representation of the average is not defined in this case.