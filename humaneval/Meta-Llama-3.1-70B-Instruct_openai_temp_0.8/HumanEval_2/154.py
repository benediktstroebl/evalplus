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
    """
    if number < 0:
        raise ValueError("Input number must be positive")

    # Calculate the integer part of the number
    integer_part = int(number)

    # Calculate the decimal part by subtracting the integer part from the original number
    decimal_part = number - integer_part

    return decimal_part


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.25))  # Expected output: 0.25
print(truncate_number(5.0))  # Expected output: 0.0
```