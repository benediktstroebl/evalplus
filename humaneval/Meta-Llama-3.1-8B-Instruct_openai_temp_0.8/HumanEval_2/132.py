```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    # Use the built-in floor function to get the integer part of the number
    integer_part = int(number // 1)
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.75))  # Output: 0.75
```

This script defines a function `truncate_number` that takes a floating-point number as input and returns its decimal part. It uses the built-in `int` function with the floor division operator (`//`) to get the integer part of the number, and then subtracts this integer part from the original number to get the decimal part. The script also includes example usage and a docstring that explains the function's purpose, parameters, return value, and examples.