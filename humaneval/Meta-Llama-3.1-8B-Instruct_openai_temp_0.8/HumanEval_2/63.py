```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    # Subtract the integer part to get the decimal part
    decimal_part = number - int(number)
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5))    # Expected output: 0.0
```

In this script, we use the built-in `int()` function to convert the floating point number to an integer, effectively removing the decimal part. Then we subtract this integer from the original number to get the decimal part. The `int()` function truncates towards zero, so for positive numbers, this effectively gives us the decimal part.