```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number: A positive floating point number.

    Returns:
        The decimal part of the number.
    """
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a positive float or int")
    
    # Use the built-in modulo operator to get the decimal part
    # The modulo operator (%) returns the remainder of the division
    # When dividing by 1, the remainder is the decimal part
    decimal_part = number % 1
    
    return decimal_part


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.25))  # Expected output: 0.25
print(truncate_number(7))  # Expected output: 0.0
```