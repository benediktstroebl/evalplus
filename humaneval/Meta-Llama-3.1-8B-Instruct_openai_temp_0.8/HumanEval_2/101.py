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
    # Use the modulo operator to get the decimal part of the number
    decimal_part = number - int(number)
    
    # Return the decimal part
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```

This script defines a function `truncate_number` that takes a positive floating-point number as input and returns its decimal part. The decimal part is obtained by subtracting the integer part of the number from the number itself. The function is then tested with the example input `3.5`, which is expected to produce an output of `0.5`.