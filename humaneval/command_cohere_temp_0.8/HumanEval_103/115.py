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
    
    total = (n + m) // 2
    count = m - n + 1
    average = total // count
    return bin(round(average))[2:]
```

This function accepts two integers, `n` and `m`, as parameters. It returns the binary string representation of the rounded average of the integers ranging from `n` to `m` (inclusive), or `-1` if `n` is greater than `m`. The solution leverages Python's built-in arithmetic and binary string capabilities to deliver the result. 

The function includes a docstring for clarity, and the `round` function is used to round the average to the nearest integer. The result is then converted to a binary string using Python's `bin` function.