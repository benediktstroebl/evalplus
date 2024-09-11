```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
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
    integer_part = int(number)
    return round(number - integer_part, 10)


# Test the function
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(4.24))  # Output: 0.24
print(truncate_number(10.0))  # Output: 0.0
```

This Python script defines a function `truncate_number` that takes a positive floating point number and returns its decimal part. The function works by subtracting the integer part of the number from the original number and rounding the result to 10 decimal places. This ensures that the decimal part is accurate to 10 decimal places. The script includes docstrings to explain the purpose and usage of the function, as well as example usage and test cases to demonstrate its behavior.