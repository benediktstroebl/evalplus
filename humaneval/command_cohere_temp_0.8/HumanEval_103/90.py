Here's a Python script that includes a function `rounded_avg(n, m)` that solves the problem:
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

The function first computes the average of the integers from `n` to `m`, rounds it to the nearest integer, and then converts the result to binary. If `n` is greater than `m`, the function returns -1. You can use this function to solve the given problem statement. 

This approach assumes that the given values `n` and `m` are valid positive integers, and it handles edge cases such as `n` being greater than `m` correctly.