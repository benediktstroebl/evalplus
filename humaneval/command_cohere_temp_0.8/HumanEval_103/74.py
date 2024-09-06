Here's a Python script with a self-contained function `rounded_avg` that solves the problem:
```python
def rounded_avg(n, m):
    """
    Compute the average of the integers from n through m (including n and m) and 
    round the answer to the nearest integer before converting it to binary. 
    Returns -1 if n is greater than m.
    """
    if n > m:
        return -1
    total = (n + m) // 2  # Average is the middle value between n and m
    return format(round(total), 'b')
```

This function takes in two positive integers, n and m, and calculates the average of the integers between them. It then rounds the average to the nearest integer and converts it to binary. If n is greater than m, it returns -1.

The `format` function is used to convert the rounded average to a binary string. The `round` function is used to round the floating-point number to the nearest integer.