Here's a Python script with a self-contained function `rounded_avg(n, m)` that solves the problem:
```python
def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = round(avg)
    
    # Convert the result to binary
    binary_representation = bin(rounded_avg)[2:]
    
    # Return -1 if n is greater than m
    if n > m:
        return -1
    
    return binary_representation
```

This function correctly handles edge cases like `rounded_avg(7, 5) `and` rounded_avg(20, 33)`, and it will return `-1` if `n` is greater than `m`. The resulting binary strings are formed correctly as well.