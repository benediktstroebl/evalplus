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
    # Use the built-in int function to truncate the integer part, 
    # then subtract this value from the original number to get the decimal part
    return number - int(number)

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.24))  # Output: 0.24
print(truncate_number(10.0))  # Output: 0.0
```

This script defines the `truncate_number` function and includes a docstring that explains its purpose, parameters, and return value. The function uses the built-in `int` function to truncate the integer part of the input number, and then subtracts this value from the original number to get the decimal part. The script also includes some test cases to demonstrate the function's behavior.