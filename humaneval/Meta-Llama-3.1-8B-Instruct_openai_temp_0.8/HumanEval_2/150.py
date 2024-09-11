### Truncating Decimal Part of a Number
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
    # Subtract the integer part from the number to get the decimal part
    return number - int(number)

# Example usage:
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.0))  # Output: 0.0
print(truncate_number(10.75))  # Output: 0.75
```
This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The decimal part is obtained by subtracting the integer part of the number (obtained using the built-in `int` function) from the number itself. The example usage demonstrates how to use this function with different inputs.