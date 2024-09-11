```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): The input floating point number.

    Returns:
        float: The decimal part of the input number.
    """
    # Check if the input number is positive
    if number < 0:
        raise ValueError("Input number must be positive")

    # Use the modulo operator to get the decimal part
    # This works because the modulo operation gives the remainder of the division
    # of the number by 1, effectively removing the integer part
    decimal_part = number % 1

    return decimal_part


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.25))  # Expected output: 0.25
print(truncate_number(7.0))  # Expected output: 0.0

# Test error handling
try:
    print(truncate_number(-1.5))
except ValueError as e:
    print(e)  # Expected output: Input number must be positive
```