```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into 
    an integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.0))  # Expected output: 0.0
print(truncate_number(5.75))  # Expected output: 0.75
```

In this script, we use the `int()` function to convert the given number to an integer, effectively rounding down to the nearest whole number. Then we subtract this integer from the original number to get the decimal part. The result is then returned by the function.