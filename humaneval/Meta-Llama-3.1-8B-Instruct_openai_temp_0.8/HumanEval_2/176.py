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
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - int(number)
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(5.0))  # Expected output: 0.0
print(truncate_number(7.23))  # Expected output: 0.23
```

This script defines a function `truncate_number` that calculates the decimal part of a given positive floating point number by subtracting its integer part from the number itself. The function is then tested with some examples to demonstrate its usage.