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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    if number < 0:
        raise ValueError("Input number must be a positive floating point number.")
    
    # Get the integer part of the number
    integer_part = int(number)
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.25))  # Expected output: 0.25
print(truncate_number(7.0))  # Expected output: 0.0

# Test with invalid input
try:
    print(truncate_number(-3.5))
except ValueError as e:
    print(e)  # Expected output: Input number must be a positive floating point number.
```