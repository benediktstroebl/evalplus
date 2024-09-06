Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer. Convert that integer to binary and 
    return as a string. If n is greater than m, return -1 as a string.
    """
    if n > m:
        return "-1"
    total = (n + m) // 2  # Average the sum of integers from n through m
    rounded = round(total)
    binary = bin(rounded)[2:]  # Convert to binary and remove '0b'
    return binary
```

This function accurately computes the average of the specified range and returns the result in binary format. It also handles the condition where the lower bound is larger than the upper bound, returning "-1" in this case.