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
    # Use the built-in int function to truncate the number
    # The int function forces the decimal part of a float to become zero
    truncated_number = int(number)
    # Use the subtraction operator to subtract the truncated number from the original number to get the decimal part
    decimal_part = number - truncated_number
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
```

Note that this script uses the built-in `int` function to truncate the number to the largest integer smaller than the given number, and then calculates the decimal part by subtracting the truncated number from the original number.