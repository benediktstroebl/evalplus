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

    Raises:
        ValueError: If the number is not positive.
    """
    if number <= 0:
        raise ValueError("The number must be positive.")

    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - int(number)

    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.99))  # Expected output: 0.99
```