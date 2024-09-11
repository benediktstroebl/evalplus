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
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a non-negative number")

    # Calculate the integer part of the number
    integer_part = int(number)

    # Calculate the decimal part of the number
    decimal_part = number - integer_part

    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.9))  # Expected output: 0.9
```

This script defines a function `truncate_number` that calculates the decimal part of a given non-negative number. It first checks if the input is a non-negative number and raises a `ValueError` if not. Then, it calculates the integer part of the number by converting it to an integer, and calculates the decimal part by subtracting the integer part from the original number. Finally, it returns the decimal part.

The script also includes test cases to demonstrate the function's usage.