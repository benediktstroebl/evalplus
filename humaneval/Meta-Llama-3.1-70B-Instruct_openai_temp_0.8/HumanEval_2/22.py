```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals 
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
    # Use the built-in modulo operator to get the decimal part of the number
    # This works because the decimal part is always the remainder when 
    # the number is divided by 1
    decimal_part = number % 1
    
    # If the decimal part is 0, but the input number was not an integer, 
    # then the number was something like 3.0, which we want to return as 0.0
    # However, in Python 3, the modulo operator returns a result with the 
    # same sign as the divisor (1 in this case), so we need to handle negative 
    # numbers separately
    if decimal_part == 0 and number!= int(number):
        decimal_part = 0.0
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.0))  # Expected output: 0.0
print(truncate_number(5))    # Expected output: 0.0
```