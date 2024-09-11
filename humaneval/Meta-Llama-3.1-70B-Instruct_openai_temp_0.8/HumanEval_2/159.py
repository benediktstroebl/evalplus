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
    # Calculate the integer part of the number
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Expected output: 0.5
print(truncate_number(10.23))  # Expected output: 0.23
```

This script defines a function `truncate_number` that takes a positive floating point number as input, calculates its decimal part, and returns it. The function uses type hints to specify the type of the input parameter and the return value. It includes a docstring that provides a description of the function, its parameters, its return value, and an example usage.

The function works by first calculating the integer part of the number using the built-in `int` function, which truncates the number to the nearest integer. Then, it calculates the decimal part by subtracting the integer part from the original number.

The script also includes some test cases to demonstrate the usage of the function.