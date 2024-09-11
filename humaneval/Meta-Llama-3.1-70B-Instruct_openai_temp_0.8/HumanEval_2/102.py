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
    """
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - int(number)
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. The decimal part is obtained by subtracting the integer part of the number from the number itself. The integer part is obtained using the built-in `int()` function, which truncates the decimal part.