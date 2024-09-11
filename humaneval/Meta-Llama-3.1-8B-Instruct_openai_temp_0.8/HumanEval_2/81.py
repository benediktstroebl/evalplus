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
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(4.25))  # Expected output: 0.25
```

This script defines a function `truncate_number` that takes a positive float as input, calculates its integer part, and returns the decimal part. The example use cases demonstrate the function's behavior with different inputs.