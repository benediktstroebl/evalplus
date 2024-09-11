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
    # Use the modulo operator to get the decimal part
    # The modulo operator returns the remainder of the division
    # Since we're dividing by 1, the remainder is the decimal part
    decimal_part = number % 1
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.8))  # Output: 0.8
print(truncate_number(7.2))   # Output: 0.2
```