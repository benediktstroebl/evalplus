```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    an integer part (largest integer smaller than given number) and decimals 
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.
    
    Example:
    >>> truncate_number(3.5)
    0.5
    """
    # Calculate the integer part using the built-in int function, which truncates the decimal part
    integer_part = int(number)
    
    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    
    # Return the decimal part
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(3.12))  # Expected output: 0.12
```

This Python script defines a function `truncate_number` that takes a positive floating point number as input, truncates its decimal part, and returns the remaining decimal part. The function uses the built-in `int` function to calculate the integer part and then subtracts this integer part from the original number to get the decimal part. The script also includes example use cases to demonstrate the function's behavior.