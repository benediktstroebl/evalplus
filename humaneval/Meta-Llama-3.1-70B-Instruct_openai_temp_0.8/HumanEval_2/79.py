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
        ValueError: If the input number is not positive.

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    if number <= 0:
        raise ValueError("Input number must be positive")

    # Calculate the integer part of the number
    integer_part = int(number)

    # The decimal part is the difference between the original number and its integer part
    decimal_part = number - integer_part

    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(7.8))  # Output: 0.8
print(truncate_number(1.2))  # Output: 0.2
```