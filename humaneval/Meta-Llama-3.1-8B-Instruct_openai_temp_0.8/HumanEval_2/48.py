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
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.7))  # Expected output: 0.7
```

This script defines a function `truncate_number` that takes a positive floating point number as input, subtracts the integer part of the number from the original number to get the decimal part, and returns the result. The function includes a docstring to provide clear documentation about its purpose, parameters, and return value. The script also includes example usage of the function.