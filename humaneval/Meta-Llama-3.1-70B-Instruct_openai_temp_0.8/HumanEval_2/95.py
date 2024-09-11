```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    >>> truncate_number(3.5)
    0.5
    """
    # Use the modulus operator to find the decimal part
    # The modulus operator returns the remainder of the division
    # Since the integer part is the quotient of the division by 1, 
    # the remainder is the decimal part
    decimal_part = number % 1
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.25))  # Expected output: 0.25
print(truncate_number(7.0))  # Expected output: 0.0
```