Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = ((n + m) // 2) if n != m else n if n > m else m
    rounded_avg = round(avg)
    
    # Convert the integer to binary
    binary = bin(rounded_avg)[2:]
    
    # Return -1 if n is greater than m
    return "-1" if n > m else binary
```

The `rounded_avg` function calculates the average of the integers between `n` and `m`, rounds it to the nearest integer, and then converts that integer to binary. If `n` is greater than `m`, it returns `-1` as specified in the problem statement. This function can be invoked with various arguments to test its behavior against the given examples provided in the problem statement.