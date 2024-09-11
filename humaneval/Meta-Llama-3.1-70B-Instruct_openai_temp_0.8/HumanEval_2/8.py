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
    # Check if the number is positive
    if number < 0:
        raise ValueError("Input number must be positive")

    # Use the built-in math.floor function to get the integer part
    # and subtract it from the original number to get the decimal part
    import math
    decimal_part = number - math.floor(number)
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
```

This script defines a function `truncate_number` that takes a positive floating point number as input and returns its decimal part. It first checks if the input number is positive and raises a `ValueError` if it's not. It then uses the `math.floor` function to get the integer part of the number, subtracts it from the original number to get the decimal part, and returns the result. Finally, it tests the function with the example input `3.5` and prints the expected output `0.5`.