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
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Input must be a non-negative number")

    # Get the integer part of the number using the int() function
    integer_part = int(number)
    
    # Calculate the decimal part by subtracting the integer part from the number
    decimal_part = number - integer_part
    
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
```

This script defines a function `truncate_number()` that takes a non-negative floating point number as input and returns its decimal part. The function first checks if the input is a non-negative number, then calculates the integer part using the `int()` function, and finally calculates the decimal part by subtracting the integer part from the number. The function includes a docstring with a detailed description, arguments, return values, and an example usage. The script also includes a test case to demonstrate the function's usage.