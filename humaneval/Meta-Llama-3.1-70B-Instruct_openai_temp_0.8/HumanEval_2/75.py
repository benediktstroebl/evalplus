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
        ValueError: If the number is not a positive floating point number.
    """
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError("Input must be a positive floating point number")

    # Use the modulo operator to get the decimal part
    # The modulo operator returns the remainder of the division of number by 1
    decimal_part = number % 1

    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.25))  # Output: 0.25
print(truncate_number(7))  # Output: 0.0
```