### Truncate Number Function
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
    integer_part = int(number)  # Convert number to integer
    decimal_part = number - integer_part  # Calculate decimal part
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.2))  # Expected output: 0.2
print(truncate_number(5.0))  # Expected output: 0.0
```

This script defines a function `truncate_number` that calculates and returns the decimal part of a given positive floating point number. It does this by subtracting the integer part of the number (obtained by converting to an integer) from the original number. The function includes docstrings for documentation and provides example use cases.