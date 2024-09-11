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
    # Calculate the integer part using the int() function
    integer_part = int(number)
    # Subtract the integer part from the number to get the decimal part
    decimal_part = number - integer_part
    return decimal_part

# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(10.7))  # Output: 0.7
```

This Python script defines a function `truncate_number()` that takes a positive float as input and returns its decimal part. It uses the built-in `int()` function to calculate the integer part of the number, and then subtracts this integer part from the original number to obtain the decimal part. The function includes a docstring that provides a description of what the function does, its arguments, return value, and includes example use cases.