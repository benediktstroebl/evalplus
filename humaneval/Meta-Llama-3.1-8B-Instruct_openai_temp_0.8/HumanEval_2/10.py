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
    return number - int(number)

# Example usage
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(9.99))  # Output: 0.99
print(truncate_number(1.0))  # Output: 0.0
```

This script uses the subtraction operation between the input number and its integer part to calculate the decimal part. The `int(number)` function truncates the decimal part, effectively removing it, leaving only the integer part. Subtracting the integer part from the original number leaves only the decimal part, which is then returned.