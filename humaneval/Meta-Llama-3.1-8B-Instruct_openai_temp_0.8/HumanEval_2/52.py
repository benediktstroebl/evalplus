### Truncate Decimal Part of a Floating Point Number
```python
def truncate_number(number: float) -> float:
    """Given a positive floating point number, return the decimal part of the number.

    The decimal part is the leftover part after decomposing the number into
    its integer part (largest integer smaller than given number) and decimals.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
```