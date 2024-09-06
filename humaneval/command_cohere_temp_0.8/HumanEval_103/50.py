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

The provided code defines a function `rounded_avg` that takes in two integers `n` and `m` and operates as follows: it calculates the average of the integers from `n` to `m` (including both `n` and `m`), rounds the average to the nearest integer, converts the rounded value to a binary representation, and returns this binary string. If `n` is greater than `m`, it returns -1. 

The code is encapsulated in a self-contained Python script, making it independent and easy to execute. When executed, it will produce the binary representation of the rounded average as expected in the problem statement.