```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it returns the decimal part.

    The decimal part is obtained by subtracting the integer part from the number.

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
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(5.0))  # Output: 0.0
print(truncate_number(7.23))  # Output: 0.23
```

This script defines a function `truncate_number` that takes a positive floating point number and returns its decimal part. The decimal part is obtained by subtracting the integer part of the number from the number itself. This is achieved using the built-in `int` function in Python, which truncates the decimal part of a number. The script includes example use cases to demonstrate the function's behavior.