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
    """
    # Use the modulo operator to get the decimal part
    # The modulo operator returns the remainder of the division of the number by 1
    # This effectively removes the integer part and leaves the decimal part
    return number % 1


# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.25))  # Expected output: 0.25
print(truncate_number(0.75))  # Expected output: 0.75
```