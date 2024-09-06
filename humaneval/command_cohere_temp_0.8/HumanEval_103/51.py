Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    # Compute the average and round it to the nearest integer
    avg = (n + m) // 2
    rounded_avg = int(round(avg))
    
    # Convert the rounded average to binary
    binary_representation = bin(rounded_avg)[2:]
    
    # Return -1 if n is greater than m
    if n > m:
        return -1
    
    return binary_representation
```

This script assumes that n and m are both positive integers. The function computes the average of the two integers and rounds it to the nearest integer before converting it to binary. It returns -1 if n is greater than m, and the binary representation otherwise. 

Let's say the result of `rounded_avg(n, m)` is `0b11010`. This can be interpreted as follows: 
- The average of 20 and 33 is 30, which gets rounded to the nearest integer, also 30. 
- The binary representation of 30 is `0b11010`, where `0b` specifies that this is a binary number and the `11010` are the corresponding binary digits. 

Please note that this implementation assumes that the input is valid, meaning that the input integers are strictly positive. You can add additional checks to verify this before executing the function.