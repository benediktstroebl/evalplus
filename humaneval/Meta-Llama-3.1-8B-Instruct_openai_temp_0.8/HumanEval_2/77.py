```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Args:
        number (float): Positive floating point number.

    Returns:
        float: Decimal part of the number.

    Example:
        >>> truncate_number(3.5)
        0.5
    """
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - int(number)
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```

This Python script defines a function `truncate_number` that calculates the decimal part of a given positive floating point number. The decimal part is calculated by subtracting the integer part (obtained using `int(number)`) from the number itself. The function returns the calculated decimal part. The script also includes an example usage of the function.