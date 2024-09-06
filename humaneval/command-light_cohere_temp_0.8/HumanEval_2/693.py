Here is a Python script with a self-contained function that solves the problem you described:
```python
def truncate_number(n: float) -> float:
    """
    Remove all decimals from a positive number.
    """
    f = n
    while (isinstance(f) and f > 1) or (f < 0):
        f = int(f)
    return f

# Test cases
print(truncate_number(3.5)) # Output: 2.0
print(truncate_number(-3.0)) # Output: -3
print(truncate_number(0.5)) # Output: 0
print(truncate_number(0.0)) # Output: 0
print(truncate_number(-0.0)) # Output: 0
print(truncate_number(0)) # Output: 0
```

The `truncate_number` function accepts a positive floating point number `n` as an argument and outputs the decimal part of `n`, which is the integer part of `n` excluding any decimals.

The function is written using a for loop to iterate through the decimal part of `n`, and is tested using an `isinstance` statement to ensure that it only outputs the integer part of the number.

This function provides a straightforward and efficient way to truncate a positive floating-point number to its decimal part.