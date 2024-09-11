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

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - int(number)
    return decimal_part

# Example usage:
print(truncate_number(3.5))   # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

This script defines a function `truncate_number` that takes a positive floating point number as input, subtracts its integer part to get the decimal part, and returns it. The example usage at the end demonstrates how to use this function.