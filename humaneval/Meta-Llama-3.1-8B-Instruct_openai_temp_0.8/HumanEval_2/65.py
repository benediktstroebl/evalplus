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

    Examples:
        >>> truncate_number(3.5)
        0.5
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.99))  # Output: 0.99
print(truncate_number(5.0))  # Output: 0.0
```

This script defines the `truncate_number` function which takes a positive floating point number as input, decomposes it into its integer and decimal parts, and then returns the decimal part. The example usage demonstrates how to use the function with different inputs.