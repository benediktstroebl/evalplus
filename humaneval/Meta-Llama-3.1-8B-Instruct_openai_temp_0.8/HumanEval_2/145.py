```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Use the built-in int function to truncate the number
    # The int function rounds down to the nearest whole number
    truncated_number = int(number)
    
    # Subtract the truncated number from the original number to get the decimal part
    decimal_part = number - truncated_number
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.7))  # Expected output: 0.7
```

This script defines a function `truncate_number` that takes a floating-point number as input and returns the decimal part of that number. It uses the built-in `int` function to truncate the number to the nearest whole number, and then subtracts this truncated number from the original number to get the decimal part. The function is then tested with a few example inputs.