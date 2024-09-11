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
print(truncate_number(10.7))  # Expected output: 0.7
print(truncate_number(5.0))  # Expected output: 0.0
```

In this script, we first calculate the integer part of the number using the built-in `int()` function. Then, we subtract the integer part from the original number to get the decimal part. Finally, we return the decimal part. The test cases at the end demonstrate the function's usage and expected outputs.