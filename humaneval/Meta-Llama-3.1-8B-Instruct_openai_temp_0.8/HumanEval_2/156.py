```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    """
    # Ensure the number is positive
    number = abs(number)
    
    # Separate the integer and decimal parts
    integer_part = int(number)
    decimal_part = number - integer_part
    
    # Return the decimal part
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(10.2))  # Outputs: 0.2
print(truncate_number(45.0))  # Outputs: 0.0
```