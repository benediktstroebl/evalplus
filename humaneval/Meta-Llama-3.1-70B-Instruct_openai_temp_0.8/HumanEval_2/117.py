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
    # Use the modulo operator to get the decimal part
    # The modulo operator returns the remainder of the division
    # of the number by 1, which effectively removes the integer part
    decimal_part = number % 1
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.23))  # Output: 0.23
print(truncate_number(1.0))  # Output: 0.0
```