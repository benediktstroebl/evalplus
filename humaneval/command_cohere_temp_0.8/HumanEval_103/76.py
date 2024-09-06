Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the rounded average to binary
    binary_representation = bin(rounded_avg)[2:]
    
    # Return -1 if n is greater than m
    if n > m:
        return -1
    else:
        return binary_representation
```

The given Python script defines a function `rounded_avg` that takes in two integers `n` and `m` as parameters. It calculates the average of the integers from `n` to `m` (inclusive), rounds it to the nearest integer, and then represents the result in binary format. If `n` is greater than `m`, it returns `-1` as the binary representation. To achieve this, the function utilizes built-in functions like `round()` and `bin()` to perform the necessary operations and conversion.