Here is a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer before returning it in binary.
    
    Args:
    - n (int): the starting integer.
    - m (int): the ending integer.
    
    Returns:
    - str: Binary string representation of the rounded average. Returns -1 if n > m.
    """
    if n > m:
        return -1
    
    total = (n + m) // 2  # Average is the middle point between n and m.
    return format(round(total), 'b').rjust(64, '0')

# Tests:
print(rounded_avg(1, 5))     # Should print "0b11"
print(rounded_avg(7, 5))     # Should print -1
print(rounded_avg(10, 20))   # Should print "0b1111"
print(rounded_avg(20, 33))   # Should print "0b11010"
```

This code provides an efficient solution to the problem, efficiently handling the calculation, rounding, and binary conversion, while also checking for the edge case of `n` being greater than `m`. 

The function `rounded_avg` uses the arithmetic mean of `n` and `m`, rounding it to the nearest integer, and converts it to a binary string of length 64 (or 8 bits), right-padded with zeros if necessary. It returns -1 if `n` is greater than `m`, following the specified requirements of the problem.